#!/usr/bin/python3 -B

from sys import stderr
from itertools import starmap, combinations
from operator import truediv, floordiv
from datetime import timezone, datetime
from os.path import abspath, basename
from hashlib import md5
from struct import unpack
from argparse import ArgumentParser
from math import radians, cos, sin, asin, sqrt
from collections import defaultdict
from xml.sax.saxutils import escape as xmlentityize
from urllib.parse import quote as urlquote

import piexif
import simplekml

# Constants per https://exiftool.org/TagNames/GPS.html
GPSLatitudeRef = 1
GPSLatitude = 2
GPSLongitudeRef = 3
GPSLongitude = 4
GPSAltitudeRef = 5
GPSAltitude = 6
GPSTimeStamp = 7
GPSMapDatum = 0x12
GPSDateStamp = 0x1d


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance (in m) between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))
    return 6371e3 * c


def barf(*args):
    print(*args, file=stderr, flush=True)


def exifnuggets(filepath: str):
    GPS = piexif.load(filepath)['GPS']
    res = {}

    def decimaldegrees(lat_or_lon: int):
        degrees, minutes, seconds = starmap(truediv, GPS[lat_or_lon])
        return degrees + minutes / 60 + seconds / 3600

    try:
        res['lat'] = {b'N': 1, b'S': -1}[GPS[GPSLatitudeRef]] * decimaldegrees(GPSLatitude)
        res['lon'] = {b'E': 1, b'W': -1}[GPS[GPSLongitudeRef]] * decimaldegrees(GPSLongitude)
    except KeyError:
        return  # to place this on a map, need at least lat & lon!
    try:
        res['altitude'] = {1: -1, 0: 1}[GPS[GPSAltitudeRef]] * truediv(*GPS[GPSAltitude])
    except KeyError:
        pass  # no altitude, fine
    try:
        datepart = map(int, GPS[GPSDateStamp].decode('ascii').split(':'))
        timepart = starmap(floordiv, GPS[GPSTimeStamp])
        res['timestamp'] = datetime(*datepart, *timepart, tzinfo=timezone.utc)
    except KeyError:
        pass  # no timestamp, fine

    if not GPS.get(GPSMapDatum) == b'WGS-84':
        barf('%s: Datum is not WGS-84' % filepath)

    return res


def text2kmlcolor(text: str):
    return simplekml.Color.rgb(*unpack('3B13x', md5(text.encode('utf-8')).digest()))


def gen_gpsinfos(filelist):
    for filepath in filelist:
        gpsinfo = {}
        try:
            gpsinfo = exifnuggets(filepath)
        except piexif._exceptions.InvalidImageDataError:
            barf('%s: Not JPEG or TIFF' % filepath)
            continue
        except Exception as err:
            barf(f'{filepath}: Error while extracting EXIF/GPS: {err}')
            continue
        if not gpsinfo:
            barf('%s: No GPS info' % filepath)
            continue
        yield (filepath, gpsinfo)


def main(filelist: list, maxw: int, maxh: int, bunchup: int):
    infos = {filepath: info for filepath, info in sorted(gen_gpsinfos(filelist), key=lambda stuff: stuff[1]['timestamp'])}

    # calculate distances & create spatial clusters
    dists = [(f1, f2, haversine(infos[f1]['lon'], infos[f1]['lat'], infos[f2]['lon'], infos[f2]['lat'])) for f1, f2 in combinations(infos.keys(), 2)]
    distmap = defaultdict(dict)
    clusters = defaultdict(set)
    for f1, f2, dist in dists:
        distmap[f1][f2] = dist
        distmap[f2][f1] = dist
        if dist > bunchup: continue
        clusters[f1].add(f2)
        clusters[f2].add(f1)

    kml = simplekml.Kml()
    seen = set()  # track which files we've handled

    for filepath, info in infos.items():
        if filepath in seen: continue  # already handled
        cluster = clusters[filepath]
        cluster -= seen  # skip files already handled (as part of other clusters)
        cluster.add(filepath)
        seen |= cluster  # mark all in cluster as handled

        # sort by time taken, filename
        clusterfiles = {fname: infos[fname] for fname in sorted(cluster, key=basename)}
        clusterfiles = dict(sorted(clusterfiles.items(), key=lambda pair: pair[1].get('timestamp', datetime(1, 1, 1))))

        # within the cluster, find the most central point and use its coordinates as the coordinates of the whole cluster
        mostcentral = sorted(((f1, sum((distmap[f1].get(f2, 0) for f2 in cluster))) for f1 in cluster), key=lambda pair: pair[1])[0][0]

        # fiddly bit to arrive at a nice point name, depending on how many files and whether there are timestamps available
        tstamps = sorted(filter(None, (info.get('timestamp') for info in clusterfiles.values())))
        pointfile_basename = basename(filepath)
        pointname = pointfile_basename
        if len(cluster) > 1:
            pointname = "%d pics" % len(cluster)
        if tstamps:
            tmin, tmax = tstamps[0].date(), tstamps[-1].date()
            if tmin == tmax:
                pointname += f' @ {str(tmin)}'
            else:
                pointname += f' @ {str(tmin)} — {str(tmax)}'

        point = kml.newpoint(name=pointname)
        gpsinfo = infos[mostcentral]
        point.coords = [tuple((round(num, 6) for num in (gpsinfo['lon'], gpsinfo['lat'], gpsinfo.get('altitude', 0))))]  # https://xkcd.com/2170/
        point.style = simplekml.Style()
        mycolor = text2kmlcolor(pointfile_basename)
        point.style.labelstyle.color = mycolor
        point.style.iconstyle.color = mycolor
        point.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/camera.png'
        imagelinks = []
        # create the minipage with the pictures
        for cfname, cinfo in clusterfiles.items():
            fullpath, thebasename = abspath(cfname), basename(cfname)
            title = thebasename
            if 'timestamp' in cinfo:
                title = f"""{thebasename} @ {cinfo['timestamp'].isoformat()}"""
            imagelinks.append(f'''<h1>{xmlentityize(title)}</h1><img style="max-width:{maxw}; max-height:{maxh}px" src="file://{urlquote(fullpath)}">''')
        point.description = F'''<![CDATA[{''.join(imagelinks)}]]>'''

    print(kml.kml())


def cli():
    parser = ArgumentParser(description="Generates a .kml geoindex (on stdout) of photographs based on GPS information in EXIF tags.")
    parser.add_argument('-x', '--maxwidth', default=1200, type=int, help="Limit picture display width to N pixels (1200 by default)")
    parser.add_argument('-y', '--maxheight', default=700, type=int, help="Limit picture display height to N pixels (700 by default)")
    parser.add_argument('-b', '--bunchup', default=10, type=int, help="Form clusters of pictures within N meters of eachother (10 by default)")
    parser.add_argument('files', nargs='+', metavar='FILE')
    args = parser.parse_args()
    main(args.files, args.maxwidth, args.maxheight, args.bunchup)


if __name__ == '__main__':
    cli()