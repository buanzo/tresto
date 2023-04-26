# Tresto

Tresto is a Python library that integrates with Trello to provide advanced
functionality for unit testing.  With Tresto, you can create Trello cards
for each test automatically, and these cards will be moved to the
appropriate list based on the test results.  This makes Tresto an ideal tool
for test-driven development, as it provides a convenient and visual way to
monitor the progress of your tests.

## Installation

You can install Tresto using pip:

```shell
pip3 install tresto
```

## Usage

Using Tresto is easy.  Simply create a TrestoTestCase and write your tests
as you normally would.  However, you will need to set up your Trello API key
and token as environment variables TRELLO_API_KEY and TRELLO_API_TOKEN.

```python
from tresto import TrestoTestCase

def test_hello_world():
    assert hello_world() == "Hello World"

class TestHelloWorld(TrestoTestCase):
    auto_create_board = True
    auto_create_lists = True

    def test_hello_world(self):
        self.add_card(self.passed_list, 'Hello World Test Passed')

        result = hello_world()
        self.assertEqual(result, "Hello World")

        self.move_card(self.failed_list, self.passed_list)
```

You can then run your tests using the standard Python unittest framework.
See the tests/ subdirectory for test_hello_world.py and test_tresto.py -
Yes, that's Tresto testing itself:

```python
import os
import unittest
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
```


## Acknowledgements

Tresto is built using the [py-trello](https://github.com/sarumont/py-trello) library. Thank you to the py-trello developers for their great work!

## Contributing

Contributions are always welcome!  If you find a bug or have a suggestion
for how to improve Tresto, please open an issue [here](https://github.com/buanzo/tresto/issues).
