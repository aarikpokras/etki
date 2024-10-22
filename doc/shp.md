The shape module allows the user to create simple 2D shapes like a circle or rectangle.

Currently, the shapes include:
* Circles
* Rectangles
* Rounded rectangles

## Usage
To create shapes, use:
```py
Shape(args)
```
Replacing `Shape` with the name of the shape and `args` with the arguments.

## `Rect`
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

## `Circle`
Creates a circle.
```py
class etki.shp.Circle(x, y, radius, *, color='black', fill=True)
```
The origin of this shape is the center.
|Argument|Purpose|Type|Note|
|--|--|--|--|
|`x`|Sets how far from the left the Circle is|float|
|`y`|Sets how far from the bottom the Circle is|float|
|`radius`|Sets how wide the Circle is from the center|float|
|`color`|Sets the color of the Circle|str|Optional|
|`fill`|Sets whether `color` is the border color (False) or the fill color (True)|bool|Optional|

## `Polygon`
A path that creates a shape.
```py
class etki.shp.Polygon(vertices, *, fillcolor='black', bordercolor='black')
```

|Argument|Purpose|Type|Note|
|--|--|--|--|
|`vertices`|See [vertices](#Vertices)|list|
|`fillcolor`|Sets the color of the inside of the Poylgon|str|Optional|
|`bordercolor`|Sets the color of the border of the Polygon|str|Optional|

### Vertices
The vertices should be a [list](https://www.w3schools.com/python/python_lists.asp), the contents of which should be [tuples](https://www.w3schools.com/python/python_tuples.asp) of points, e.g.
```py
Polygon(
  [
    (1, 1),
    (2, 1),
    (2, 2),
    (1, 2),
    (1, 1)
  ]
)
```
The last point should close the shape, i.e. the last point should be the same as the first.
