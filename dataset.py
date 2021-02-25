from typing import List, Dict

class Route:
    streets_count: int
    streets: List[str]

    def __init__(
        self, 
        streets_count: int, 
        streets: List[str]
    ):
        self.streets_count = streets_count
        self.streets = streets


class Street:
    start: int #id intersection
    end: int #id intersection
    name: str
    time: int #time to get from start to end

    def __init__(self, start: int, end: int, name: str, time: int):
        self.start = start
        self.end = end
        self.name = name
        self.time = time


class Dataset:
    deadline: int
    intersections_count: int
    streets_count: int
    cars_count: int
    bonus_for_car: int
    streets: Dict[str, Street]
    car_routes: List[Route]

    def __init__(self, filename: str):
        with open(filename, "r") as f:
            header = f.readline()

            self.deadline, \
            self.intersections_count, \
            self.streets_count, \
            self.cars_count, \
            self.bonus_for_car = map(int, header.split())

            self.streets = dict()
            self.car_routes = list()

            for _ in range(self.streets_count):
                start, end, name, time = f.readline().split()
                start = int(start)
                end = int(end)
                time = int(time)
                self.streets[name] = Street(start, end, name, time)
            
            for _ in range(self.cars_count):
                car_route = f.readline().split()
                streets_count = car_route[0]
                streets = car_route[1:]
                self.car_routes.append(Route(int(streets_count), streets))
