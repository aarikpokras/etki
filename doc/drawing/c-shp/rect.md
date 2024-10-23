# `etki.shp.Rect`
`Rect`

Creates a rectangle.
```py
class etki.shp.Rect(x, y, width, height, *, color='black', fill=True, borderradius=0)
```
The origin for this shape is the bottom-left.
|Argument|Purpose|Type|Note|
|--|--|--|--|
|`x`|Sets how far from the left the Rect is|float|
|`y`|Sets how far from the bottom the Rect is|float|
|`width`|Sets how wide the Rect is|float|
|`height`|Sets how tall the Rect is|float|
|`color`|Sets the color of the Rect|str|Optional|
|`fill`|Sets whether `color` is the border color (False) or the fill color (True)|bool|Optional|
|`borderradius`|Sets the roundness of the corners of the rect. Also adds 0.1 units of padding|float|Optional|
