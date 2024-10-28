# `etki.shp.Rect`
`Rect`

Creates a rectangle.
```py
class etki.shp.Rect(x, y, width, height, *, fillcolor='black', bordercolor='black', borderradius=0, rotateAngle=0)
```
The origin for this shape is the bottom-left.
|Argument|Purpose|Type|Note|
|--|--|--|--|
|`x`|Sets how far from the left the Rect is|float|
|`y`|Sets how far from the bottom the Rect is|float|
|`width`|Sets how wide the Rect is|float|
|`height`|Sets how tall the Rect is|float|
|`fillcolor`|Sets the fill color of the Circle|str|Optional|
|`bordercolor`|Sets the border color of the Circle|str|Optional|
|`borderradius`|Sets the roundness of the corners of the rect. Also adds 0.1 units of padding|float|Optional|
|`rotateAngle`|Sets the angle counter-clockwise|float|Optional|
