# `etki.shp.Oval`
`Oval`

Creates an oval of a specified height and width.
```py
class etki.shp.Oval(x, y, width, height, *, color='black', fill=True, rotateAngle=0)
```
The origin of this shape is the center.
|Argument|Purpose|Type|Note|
|--|--|--|--|
|`x`|Sets how far from the left the Oval is|float|
|`y`|Sets how far from the bottom the Oval is|float|
|`width`|Sets how wide the Oval is from the center|float|
|`height`|Sets how high the Oval is from the center|float|
|`color`|Sets the color of the Oval|str|Optional|
|`fill`|Sets whether `color` is the border color (False) or the fill color (True)|bool|Optional|
|`rotateAngle`|Sets the angle counter-clockwise|float|Optional|
