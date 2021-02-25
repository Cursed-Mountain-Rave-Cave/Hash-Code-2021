from math import gcd
from functools import reduce
from dataset import Route, Street, Dataset


def bidlo(dataset: Dataset):
    intersections = [[] for _ in range(dataset.intersections_count)]
    roads = {}

    for street in dataset.streets.values():
        intersections[street.end].append(street.name)

    for route in dataset.car_routes:
        for street in route.streets:
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
