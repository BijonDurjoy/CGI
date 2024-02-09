def draw_line(points):
    max_x = max(points, key=lambda p: p[0])[0]
    max_y = max(points, key=lambda p: p[1])[1]

    console = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y in points:
        console[y][x] = '#'

    for row in console:
        print(" ".join(row))


def bresenham_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    x = x1
    y = y1
    points = [(x, y)]

    if abs(dy) <= abs(dx):
        p = 2 * dy - dx
        for _ in range(x1, x2):
            if p > 0:
                y += 1
                p -= 2 * dx
            p += 2 * dy
            x += 1
            points.append((x, y))
    else:
        p = 2 * dx - dy
        for _ in range(y1, y2):
            if p > 0:
                x += 1
                p -= 2 * dy
            p += 2 * dx
            y += 1
            points.append((x, y))

    return points


case = bresenham_line(1, 1, 8, 4)
print("Case 1 Points:", case)
print()
print("Case 1 Line Drawing:")
draw_line(case)
