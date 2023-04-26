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
pip install tresto
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
Yes, that's Tresto testing itself.


## Acknowledgements

Tresto is built using the [py-trello](https://github.com/sarumont/py-trello) library. Thank you to the py-trello developers for their great work!

## Contributing

Contributions are always welcome!  If you find a bug or have a suggestion
for how to improve Tresto, please open an issue [here](https://github.com/buanzo/tresto/issues).
