# Quickstart

![Photo of ETkI](https://bottlenose-nova-acapella.glitch.me/etki-pb.png)

**Important:** *To make a line, you must import the `etki.plot` module separately.*

### Importing all modules (May cause some bugs)
To import ETkI, with etki in your working directory, use:
```py
from etki import *
```
If it causes a bug, please make an [issue](https://github.com/aarikpokras/etki/issues/new?assignees=aarikpokras&labels=bug&projects=&template=bug_report.yml&title=%5BBrief+description+of+bug%5D).

### Importing specific modules
|Action|Module|
|--|--|
|Make a shape (rectangle, path, etc.)|`etki.shp`|
|Make a text label|`etki.txt`|
|Make a line|`etki.plot`|

You must import these modules individually, e.g.:<br />
If I was drawing a circle and a text label, I would do the following:
```py
import etki.shp # For the circle
import etki.txt # For the label
```

<!-- Add guide for how to use docs - class sig -->
