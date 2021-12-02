import unittest

from classes.day2.navigation import Navigation


class TestNavigation(unittest.TestCase):

    def test_MoveHorizontalAndDown(self):
        cut = Navigation()
        position = cut.position(["down 2", "forward 5"])
        self.assertEquals(50, position)

    def test_MoveHorizontalAndChangeDepths(self):
        cut = Navigation()
        position = cut.position(["down 4", "forward 5", "up 1"])
        self.assertEquals(100, position)

    def test_MoveSubmarine(self):
        cut = Navigation()
        position = cut.position(["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"])
        self.assertEquals(900, position)
