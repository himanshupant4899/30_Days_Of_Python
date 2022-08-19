import argparse
import random


def roll_dice():
    output = []
    for n in range(args.number):
        output.append(random.randint(1, (args.faces + 1)))
    display(output)


def display(output):
    values = ", ".join([str(x) for x in output])
    print()
    print(f"Rolls: {values}")
    print(f"Total: {sum(output)}")
    avg = sum(output) / len(output)
    print(f"Average: {round(avg, 2)}")
    log_to_file(values, output, avg)


def log_to_file(values, output, avg):
    file_name = args.logs
    with open(file_name, "a") as logs:
        logs.write(f'Rolls: {values}\nTotal: {sum(output)}\nAverage: {round(avg, 2)}\n\n')


parser = argparse.ArgumentParser(description="Simulates a CLI dice roller.")
parser.add_argument("number", type=int, help="Number of dices to be rolled at once.")
parser.add_argument(
    "-d",
    "--faces",
    type=int,
    default=6,
    help="Number of faces that the dice should have."
)

parser.add_argument(
    "-l",
    "--logs",
    type=str,
    default="rolls.txt",
    help="Specify a log file."
)

parser.add_argument(
    "-r",
    "--repeat",
    type=int,
    default=1,
    help="Number of time to roll the dice set."
)

args = parser.parse_args()

for num in range(args.repeat):
    roll_dice()






