import unittest
from budget_manager import BudgetManager

class TestBudgetManager(unittest.TestCase):
    def setUp(self):
        self.manager = BudgetManager()

    def test_budget_setting(self):
        self.manager.set_budget(1000)
        self.assertEqual(self.manager.budget, 1000)

    def test_add_expense(self):
        self.manager.add_expense("Mat", 250)
        self.assertIn("Mat", self.manager.expenses)
        self.assertEqual(self.manager.expenses["Mat"], 250)

    def test_remaining_budget(self):
        self.manager.set_budget(1000)
        self.manager.add_expense("Mat", 250)
        self.assertEqual(self.manager.get_remaining_budget(), 750)

if __name__ == '__main__':
    unittest.main()
