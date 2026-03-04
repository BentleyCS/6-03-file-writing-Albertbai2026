import random


def writeFile(inputList, fileName):
    """
    Creates a file and writes each list item on its own line.
    """
    f = open(fileName, "w")
    for item in inputList:
        # make sure everything is a string before writing
        f.write(str(item) + "\n")
    f.close()


def sortNames(fileName, targetFile):
    """
    Reads names from source file, sorts them, and writes to target file.
    """
    # read all non-empty lines
    f = open(fileName, "r")
    names = []
    for line in f:
        name = line.strip()
        if name != "":
            names.append(name)
    f.close()

    # sort names alphabetically
    names.sort()

    # write sorted names to the target file
    f = open(targetFile, "w")
    for name in names:
        f.write(name + "\n")
    f.close()


def highScore(newScore):
    """
    Adds newScore to scores.txt, then returns the average of all scores.
    """
    fileName = "scores.txt"

    # open file in append mode and add the new score
    f = open(fileName, "a")
    f.write(str(int(newScore)) + "\n")
    f.close()

    # now read all scores back from the file
    f = open(fileName, "r")
    scores = []
    for line in f:
        line = line.strip()
        if line != "":
            scores.append(int(line))
    f.close()

    if len(scores) == 0:
        return 0.0
    else:
        total = 0
        for s in scores:
            total = total + s
        average = total / len(scores)
        return average


if __name__ == "__main__":
    # example usage (not used by the tests)
    sortNames("names.txt", "namesNew.txt")
    highScore(random.randint(1, 100))
