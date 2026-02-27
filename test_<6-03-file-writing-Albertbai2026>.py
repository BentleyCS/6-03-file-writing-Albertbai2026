import unittest
from CSP_6_02_reading_files import writeFile, sortNames, highScore


class TestReadingFiles(unittest.TestCase):
    def test_writeFile(self):
        fn = "tmp_write.txt"
        data = ["Alice", 7, "Bob"]
        writeFile(data, fn)
        with open(fn, "r") as f:
            self.assertEqual(f.read(), "Alice\n7\nBob\n")

    def test_sortNames(self):
        src = "tmp_names.txt"
        dst = "tmp_names_sorted.txt"
        with open(src, "w") as f:
            f.write("Bob\nAlice\nCharlie\n")
        sortNames(src, dst)
        with open(dst, "r") as f:
            self.assertEqual(f.read(), "Alice\nBob\nCharlie\n")

    def test_highScore_appends_and_averages(self):
        # reset scores.txt so the test is predictable
        with open("scores.txt", "w") as f:
            f.write("10\n20\n30\n")
        avg = highScore(40)  # -> 25.0
        self.assertAlmostEqual(avg, 25.0)
        with open("scores.txt", "r") as f:
            self.assertEqual(f.read(), "10\n20\n30\n40\n")


if __name__ == "__main__":
    unittest.main()
