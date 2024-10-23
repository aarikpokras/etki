# shp

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
