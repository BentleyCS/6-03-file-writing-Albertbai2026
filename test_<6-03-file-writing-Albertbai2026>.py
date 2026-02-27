from CSP_6_02_reading_files import writeFile, sortNames, highScore


def test_writeFile_creates_lines():
    file_name = "test_write.txt"
    data = ["Alice", "Bob", "Charlie"]

    writeFile(data, file_name)

    with open(file_name, "r") as f:
        lines = f.readlines()

    assert lines == [name + "\n" for name in data]


def test_sortNames_sorts_into_target_file():
    source = "test_names_source.txt"
    target = "test_names_sorted.txt"

    with open(source, "w") as f:
        f.write("Bob\n")
        f.write("Alice\n")
        f.write("Charlie\n")

    sortNames(source, target)

    with open(target, "r") as f:
        result = [line.strip() for line in f if line.strip()]

    assert result == ["Alice", "Bob", "Charlie"]


def test_highScore_appends_and_averages():
    # reset scores.txt to a known state
    with open("scores.txt", "w") as f:
        f.write("10\n")
        f.write("20\n")
        f.write("30\n")

    avg = highScore(40)  # scores: 10, 20, 30, 40 → average = 25

    assert abs(avg - 25.0) < 1e-6

    with open("scores.txt", "r") as f:
        scores = [int(line.strip()) for line in f if line.strip()]

    assert scores == [10, 20, 30, 40]
