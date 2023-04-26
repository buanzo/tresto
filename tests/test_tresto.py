import os
import unittest
from trello import TrelloClient
from tresto import TrestoTestCase

class TestTresto(TrestoTestCase):

    def setUp(self):
        self.card_failed = None
        self.card_passed = None

    def test_1_board_setup(self):
        self.assertIsNotNone(self.board)
        self.assertEqual(self.board.name, self.board_name)

    def test_2_list_setup(self):
        self.assertIsNotNone(self.passed_list)
        self.assertIsNotNone(self.failed_list)
        self.assertEqual(self.passed_list.name, self.test_passed_list)
        self.assertEqual(self.failed_list.name, self.test_failed_list)

    def test_3_add_card_to_failed_list(self):
        card_name = "Test Card for FAILED List"
        self.card_failed = self.add_card(self.failed_list, card_name)
        self.assertEqual(self.card_failed.name, card_name)

    def test_4_archive_card_from_failed_list(self):
        self.card_failed.set_closed(True)
        archived_card = self.board.get_card(self.card_failed.id)
        self.assertTrue(archived_card.closed)

    def test_5_add_card_to_passed_list(self):
        card_name = "Test Card for PASSED List"
        self.card_passed = self.add_card(self.passed_list, card_name)
        self.assertEqual(self.card_passed.name, card_name)

    def test_6_archive_card_from_passed_list(self):
        self.card_passed.set_closed(True)
        archived_card = self.board.get_card(self.card_passed.id)
        self.assertTrue(archived_card.closed)

    def test_7_add_and_move_card_between_lists(self):
        card_name = "Test Card for Moving Between Lists"
        card = self.add_card(self.passed_list, card_name)
        self.move_card(card, self.failed_list)

        # Refresh card data
        card.fetch()

        self.assertEqual(card.list_id, self.failed_list.id)

if __name__ == '__main__':
    unittest.main()
