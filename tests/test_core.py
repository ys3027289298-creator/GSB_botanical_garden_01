import unittest

import core


class TestCore(unittest.TestCase):
    def test_01_no_duplicate_register(self):
        state = core.new_game()
        self.assertTrue(core.register(state, "P1"))
        self.assertFalse(core.register(state, "P1"))

    def test_02_greenhouse_capacity(self):
        state = core.new_game()
        core.transplant(state, "P1")
        core.transplant(state, "P2")
        result = core.transplant(state, "P3")
        self.assertFalse(result)

    def test_03_fee_exact(self):
        state = core.new_game()
        self.assertEqual(core.fee(state, "P1", 3), 2)

    def test_04_cancel_refunds_soil(self):
        state = core.new_game()
        state["soil"] = 90
        core.cancel(state, "P1")
        self.assertEqual(state["soil"], 100)

    def test_05_no_assign_absent_gardener(self):
        state = core.new_game()
        core.register(state, "P1")
        result = core.assign(state, "P1", "G2")
        self.assertFalse(result)

    def test_06_water_fail_no_cost(self):
        state = core.new_game()
        core.register(state, "P1")
        state["plants"]["P1"]["failed"] = True
        before = state["soil"]
        result = core.water(state, "P1")
        self.assertFalse(result)
        self.assertEqual(state["soil"], before)

    def test_07_pest_once(self):
        state = core.new_game()
        core.register(state, "P1")
        core.pest(state, "P1")
        self.assertEqual(state["plants"]["P1"]["health"], 90)

    def test_08_load_preserves_plant_id(self):
        state = core.new_game()
        state["plant_id"] = 4
        loaded = core.load_state(core.save_state(state))
        self.assertEqual(loaded["plant_id"], 4)


if __name__ == "__main__":
    unittest.main()
