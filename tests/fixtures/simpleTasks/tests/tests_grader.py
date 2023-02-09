from uuid import uuid4
import unittest
import simpleTasks as tasks


def areFilesEqual(filePath1, filePath2):
    with open(filePath1, "r") as f1:
        lines1 = f1.readlines()
    with open(filePath2, "r") as f2:
        lines2 = f2.readlines()
        return len(lines1) == len(lines2) and all(
            l1 == l2 for l1, l2 in zip(lines1, lines2)
        )


class WritePyramidsTestCase(unittest.TestCase):
    def test_writePyramids1(self):
        randomFileName = f"{str(uuid4())}.txt"
        tasks.writePyramids(randomFileName, 13, 6, "X")
        areEqual = areFilesEqual(randomFileName, f"pyramid13.txt")
        self.assertTrue(areEqual)

    def test_writePyramids2(self):
        randomFileName = f"{str(uuid4())}.txt"
        tasks.writePyramids(randomFileName, 15, 5, "*")
        areEqual = areFilesEqual(randomFileName, f"pyramid15.txt")
        self.assertTrue(areEqual)


class GetStreaksTestCase(unittest.TestCase):
    sequence = "AAASSSSSSAPPPSSPPBBCCCSSS"

    def test_getStreaks1(self):
        expectedValue = ["AAA", "SSSSSS", "A", "SS", "SSS"]
        actualValue = tasks.getStreaks(self.sequence, "SAQT")
        self.assertEqual(expectedValue, actualValue)

    def test_getStreaks2(self):
        expectedValue = ["AAA", "A", "PPP", "PP"]
        actualValue = tasks.getStreaks(self.sequence, "PAZ")
        self.assertEqual(expectedValue, actualValue)
