# Task 1

def cgi(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    x = x1
    y = y1
    D = 2 * dy - dx
    points = [(x, y)]

    for _ in range(x1, x2):
        if D > 0:
            y += 1
            D -= 2 * dx
        D += 2 * dy
        x += 1
        points.append((x, y))

    return points

print("The points are:")
print(cgi(1, 1, 8, 4))