# Test 1
array = []
array.append([])
array.append([])

array[1].append(11)

# Test 2


def geo_distance(ax, ay, bx, by):
    return((ax-bx)**2+(ay-by)**2)**(1/2)


print(geo_distance(0, 0, 3, 4))
