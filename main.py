import sys
from dataset import Street, Route, Dataset
from bidlo import bidlo

original_stdout = sys.stdout # Save a reference to the original standard output

if __name__ == "__main__":
    for filename in sys.argv[1:]:
        dataset = Dataset(filename)
        with open(filename.replace('data', 'outputs'), 'w') as f:
            sys.stdout = f # Change the standard output to the file we created.
            bidlo(dataset)
            sys.stdout = original_stdout # Reset the standard output to its original value
