import sys

class Dataset:
    deadline: int
    intersections_count: int
    streets_count: int
    cars_count: int
    bonus_for_car: int
    streets: dict
    car_routes: list

    def __init__(self):
        self.deadline = None
        self.intersections_count = None
        self.streets_count = None
        self.cars_count = None
        self.bonus_for_car = None
        self.streets = None
        self.car_routes = None


class Street:
    start: int #id intersection
    end: int #id intersection
    name: str
    time: int #time to get from start to end

    def __init__(self, start, end, name, time):
        self.start = start
        self.end = end
        self.name = name
        self.time = time


class Route:
    street_count: int
    streets: list

    def __init__(self, street_count, streets):
        self.street_count = street_count
        self.streets = streets


def datafile_names():
    return sys.argv[1:]


def dataset_from_file(filename):
    with open(filename, "r") as f:
        dataset = Dataset()

        header = f.readline()
        deadline, \
        intersections_count, \
        streets_count, \
        cars_count, \
        bonus_for_car = map(int, header.split())

        dataset.deadline = deadline
        dataset.intersections_count = intersections_count
        dataset.streets_count = streets_count
        dataset.cars_count = cars_count
        dataset.bonus_for_car = bonus_for_car
        dataset.streets = dict()
        dataset.car_routes = list()

        for _ in range(streets_count):
            start, end, name, time = f.readline().split()
            start = int(start)
            end = int(end)
            time = int(time)
            dataset.streets[name] = Street(start, end, name, time)
        
        for _ in range(cars_count):
            car_route = f.readline().split()
            street_count = car_route[0]
            streets = car_route[1:]
            dataset.car_routes.append(Route(streets_count, car_route))
        
        return dataset

if __name__ == "__main__":
    print(datafile_names())
    dataset = dataset_from_file(datafile_names()[1])
    print(dataset.__dict__)