import unittest

from classes.day3.consumption import Consumption


class TestConsumption(unittest.TestCase):
    input = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010"
    ]

    def test_MostCommonBit(self):
        input = ["00", "11", "01"]

        consumption = Consumption()

        self.assertEqual(0, consumption.mostCommonBit(input, 0))
        self.assertEqual(1, consumption.mostCommonBit(input, 1))

    def test_MostCommonBit_EqualNumber_PreferOne(self):
        input = ["00", "11", "01", "10"]

        consumption = Consumption()

        self.assertEqual(1, consumption.mostCommonBit(input, 0))
        self.assertEqual(1, consumption.mostCommonBit(input, 1))

    def test_Filter(self):
        input = ["00", "11", "01", "10"]

        consumption = Consumption()

        self.assertEqual(["00", "01"], consumption.filter(input, 0, 0))
        self.assertEqual(["11", "01"], consumption.filter(input, 1, 1))

    def test_LeastCommonBit(self):
        input = ["00", "11", "01"]

        consumption = Consumption()

        self.assertEqual(0, consumption.leastCommonBit(input, 1))
        self.assertEqual(1, consumption.leastCommonBit(input, 0))

    def test_gama(self):
        consumption = Consumption()

        self.assertEqual(22, consumption.gamma(self.input))

    def test_epsilon(self):
        consumption = Consumption()

        self.assertEqual(9, consumption.epsilon(self.input))

    def test_consumption(self):

        consumption = Consumption()

        self.assertEqual(198, consumption.powerConsumption(self.input))

    def test_oxygen(self):
        consumption = Consumption()

        self.assertEqual(23, consumption.oxygen(self.input, 0))

    def test_oxygen_singleValueLeft(self):
        consumption = Consumption()

        self.assertEqual(1, consumption.oxygen(["01"], 0))

    def test_co2(self):
        consumption = Consumption()

        self.assertEqual(10, consumption.co2(self.input, 0))

    def test_lifeSupport(self):
        consumption = Consumption()

        self.assertEqual(230, consumption.lifeSupport(self.input))