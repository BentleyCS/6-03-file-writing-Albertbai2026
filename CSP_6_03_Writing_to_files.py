import random

# You need to create your own test file for this assignment.
# Because we are dealing with both reading and writing to files. Your test file will be more complicated than it has been.


def writeFile(inputList, fileName):
    # Creates a file of the given name and adds each value from the list
    # to the file, with each line being one item from the list.
    with open(fileName, "w") as f:
        for value in inputList:
            f.write(str(value) + "\n")


def sortNames(fileName, targetFile):
    # Takes in a source file and a target file.
    # Sort all of the values from the source file and write them to the target file.
    with open(fileName, "r") as f:
        names = [line.strip() for line in f if line.strip()]

    names.sort()

    with open(targetFile, "w") as f:
        for name in names:
            f.write(name + "\n")


def highScore(newScore: int):
    # Adds a new score to the file scores.txt
    # Then returns the average score from all of the scores in scores.txt
    file_name = "scores.txt"

    # append the new score
    with open(file_name, "a") as f:
        f.write(str(newScore) + "\n")

    # read back all scores and compute average
    with open(file_name, "r") as f:
        scores = [int(line.strip()) for line in f if line.strip()]

    if not scores:
        return 0

    return sum(scores) / len(scores)


# Leave these calls if your teacher provided them
sortNames("names.txt", "namesNew.txt")
highScore(random.randint(1, 100))
