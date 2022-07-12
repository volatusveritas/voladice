import unittest

import pydice


class TestBasicRolls(unittest.TestCase):
    def test_d6_single_roll_boundaries(self):
        dice_d6_total: int = pydice.D6.roll().get_total()

        self.assertTrue(dice_d6_total >= pydice.D6._lower_limit)
        self.assertTrue(dice_d6_total <= pydice.D6._upper_limit)

    def test_d6_multi_roll_boundaries(self):
        dice_3d6_total: int = pydice.D6.rollmany(3).get_total()

        self.assertTrue(dice_3d6_total >= pydice.D6._lower_limit*3)
        self.assertTrue(dice_3d6_total <= pydice.D6._upper_limit*3)

    def test_multi_dice_roll_boundaries(self):
        multi_dice_total: int = (
            pydice.D6.roll() + pydice.D8.rollmany(2)
        ).get_total()

        self.assertTrue(multi_dice_total >= (
            pydice.D6._lower_limit + pydice.D8._lower_limit*2
        ))
        self.assertTrue(multi_dice_total <= (
            pydice.D6._upper_limit + pydice.D8._upper_limit*2
        ))


if __name__ == "__main__":
    unittest.main()
