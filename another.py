from math import gcd
from typing import List, Dict, Set, Tuple
from functools import reduce
from dataset import Route, Street, Dataset


class StreetStat:
    street: Street
    times: List[int]

    def __init__(self, street: Street):
        self.street = street
        self.times = list()


class Intersection:
    id: int
    time_to_street_set: Dict[int, Set[str]] 

    def __init__(self, id: int) -> None:
        self.id = id
        self.time_to_street_set = dict()


def another(dataset: Dataset):
    streets_stats: Dict[str, StreetStat] = dict()
    for street in dataset.streets.values():
        streets_stats[street.name] = StreetStat(street)
    
    for route in dataset.car_routes:
        time = 0
        for i, street_name in enumerate(route.streets):
            street = streets_stats[street_name].street
            if i != 0:
                time += street.time
            if i != route.streets_count - 1:
                streets_stats[street_name].times.append(time)

    intersections: List[Intersection] = [Intersection(id) for id in range(dataset.intersections_count)]

    for street_name, street_stat in streets_stats.items():
        for time in street_stat.times:
            intersection = intersections[street_stat.street.end]
            if time not in intersection.time_to_street_set:
                intersection.time_to_street_set[time] = set()
            intersection.time_to_street_set[time].add(street_name)
    
    output_intersections: List[Tuple[int, List[Tuple[str, int]]]] = list()

    for intersection in intersections:
        if len(intersection.time_to_street_set):
            used_streets: Set[str] = set()
            time_street_list: List[Tuple[int, str]] = list()

            for time, streets in sorted(intersection.time_to_street_set.items(), key=lambda x: x[0]):
                fixed_streets = streets - used_streets
                if len(fixed_streets) == 0:
                    continue
                street = fixed_streets.pop()
                used_streets.add(street)
                time_street_list.append((time+1, street))
            output_intersections.append((intersection.id, time_street_list))

    print(len(output_intersections))
    for id, time_street_list in output_intersections:
        print(id)
        print(len(time_street_list))
        for time, street in time_street_list:
            print(street, time)
