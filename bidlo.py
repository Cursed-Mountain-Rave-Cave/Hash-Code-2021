from math import gcd
from functools import reduce

d, i, s, v, f = map(int, input().split())

intersections = [[] for _ in range(i)]
roads = {}

for _ in range(s):
    b, e, name, l = input().split()
    intersections[int(e)].append(name)

for _ in range(v):
    route = input().split()
    for _, street in enumerate(route[1:]):
        if street not in roads:
            roads[street] = 0
        roads[street] += 1


out_data = {}

#TODO
#sort by num of cars 

for i, intersection in enumerate(intersections):
    route = []
    for road in set(intersection):
        if road in roads:
            route.append((road, roads[road]))
    if len(route) > 0:
        out_data[i] = route

print(len(out_data))

for key, value in out_data.items():
    print(key)
    print(len(value))
    c_gcd = reduce(gcd, map(lambda x: x[1], value))
    for street, count in value:
        print(street, count // c_gcd)
