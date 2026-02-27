import random

#You need to create your own test file for this assignment.
#Because we are dealing with both reading and writing to files. Your test file will be more complicated than it has been.

def writeFile(inputList, fileName):
    # Creates a file and writes each list item on its own line
    with open(fileName, "w") as f:
        for item in inputList:
            f.write(str(item) + "\n")


def sortNames(fileName, targetFile):
    # Reads names from source file, sorts, writes to target file
    with open(fileName, "r") as f:
        names = [line.strip() for line in f if line.strip()]

    names.sort()

    with open(targetFile, "w") as f:
        for name in names:
            f.write(name + "\n")


def highScore(newScore: int):
    # Adds newScore to scores.txt, returns average of all scores
    fileName = "scores.txt"

    # create file if missing + append
    with open(fileName, "a+") as f:
        f.write(str(int(newScore)) + "\n")

    # read all scores
    with open(fileName, "r") as f:
        scores = [int(line.strip()) for line in f if line.strip()]

    return sum(scores) / len(scores) if scores else 0.0


if __name__ == "__main__":
    sortNames("names.txt", "namesNew.txt")
    highScore(random.randint(1, 100))
