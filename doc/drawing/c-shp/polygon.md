# `etki.shp.Polygon`
`Polygon`

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
