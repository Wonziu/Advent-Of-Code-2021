## Day 9
Cool way to check neighbours of 2d array with checking edge cases.

```python=
for y in range(rows):
        for x in range(columns):
            if all(dx + x < 0 
                or dx + x >= columns 
                or dy + y < 0 
                or dy + y >= rows 
                # condition: or data[y][x] < data[y + dy][x + dx]
                for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0))):
                # expression: count += data[y][x] + 1
```
