# photokml
Generates a .kml geoindex of photographs based on GPS information in EXIF tags.

Run it on a bunch of photos, load up the .kml in Google Earth, and click the icons
to view your pictures. Screenshot:

![A photokml-generated KML file loaded up in Google Earth](https://raw.githubusercontent.com/blinkingtwelve/photokml/master/screenshot.png)

```
usage: photokml.py [-h] [-x MAXWIDTH] [-y MAXHEIGHT] [-b BUNCHUP]
                   FILE [FILE ...]

Generates a .kml geoindex (on stdout) of photographs based on GPS information
in EXIF tags.

positional arguments:
  FILE

optional arguments:
  -h, --help            show this help message and exit
  -x MAXWIDTH, --maxwidth MAXWIDTH
                        Limit picture display width to N pixels (1200 by
                        default)
  -y MAXHEIGHT, --maxheight MAXHEIGHT
                        Limit picture display height to N pixels (700 by
                        default)
  -b BUNCHUP, --bunchup BUNCHUP
                        Form clusters of pictures within N meters of eachother
                        (10 by default)
```
