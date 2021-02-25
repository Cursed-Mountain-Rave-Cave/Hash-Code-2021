import sys
from dataset import Street, Route, Dataset


if __name__ == "__main__":
    for filename in sys.argv[1:]:
        dataset = Dataset(filename)
        print(dataset.__dict__)
