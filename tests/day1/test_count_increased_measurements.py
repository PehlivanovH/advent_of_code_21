import unittest

from classes.day1.count_increased_measurements import CountIncreasedMeasurements


class TestCountIncreasedMeasurements(unittest.TestCase):

    def test_countIncreasedMeasurements(self):
        cut = CountIncreasedMeasurements()

        numberOfIncreases = cut.countIncreasedMeasurements([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])

        self.assertEqual(7, numberOfIncreases)
