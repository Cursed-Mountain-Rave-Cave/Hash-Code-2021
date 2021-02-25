d, i, s, v, f = map(int, input().split())

roads = [[] for _ in range(i)]

for _ in range(s):
    b, e, name, l = input().split()
    roads[int(e)].append(name)

for _ in range(v):
    input()

print(len(roads))

for i, roads in enumerate(roads):
    print(i)
    print(len(roads))
    for road in set(roads):
        print(road, 1)
