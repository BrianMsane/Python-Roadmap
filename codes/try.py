import argparse

parser = argparse.ArgumentParser(
    description="Learning Arguments parsing in this script as we advance our Python journey 😂"
)

parser.add_argument(
    "name", help="The name of the csv file that contains the training data", type=str
)
parser.add_argument("--dir", help="directory in which this file is stored", type=str)


args = parser.parse_args()

name = args.name
path = args.dir if args.dir else "not specified"

print(name)
print(path)
