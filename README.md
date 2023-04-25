# Tresto

Tresto is a Python library that integrates with Trello and provides additional functionality for unit testing. With Tresto, you can create Trello cards for each test, automagically, and those cards will be moved to the appropriate list based on the test result.

Ideal for development teams, management, devops, etc.

## Installation

You can install Tresto using pip:

```
pip3 install tresto
```

## Usage

To use Tresto, you need to create a Trello board and, optionally (for now and at least) two lists: "TEST PASSED" and "TEST FAILED". You also need to set up your Trello API key and token as environment variables TRELLO_API_KEY and TRELLO_API_TOKEN.

Next, you can create a unittest test class and inherit from `TrestoTestCase`. You can then implement your test cases as usual, and Tresto will take care of creating Trello cards for each test and moving them to the appropriate list based on the test result.

Here's an example of how to use Tresto:

```python
from tresto import TrestoTestCase

def hello_world():
    return "Hello World"

class TestHelloWorld(TrestoTestCase):
    board_name = 'My Trello Devops Board'
    test_passed_list = 'PASSED'
    test_failed_list = 'FAILED'

    def test_hello_world(self):
        result = hello_world()
        self.assertEqual(result, "Hello World")

```

If you are feeling lazy/productive, then you could just let Tresto create the PASSED and FAILED lists:

```python
from tresto import TrestoTestCase

def hello_world():
    return "Hello World"

class TestHelloWorld(TrestoTestCase):
    board_name = 'My Trello Board'
    auto_create_lists = True

    def test_hello_world(self):
        result = hello_world()
        self.assertEqual(result, "Hello World")

```


Wait - Feling adventurous you say? Try this:

```python
from tresto import TrestoTestCase

def hello_world():
    return "Hello World"

class TestHelloWorld(TrestoTestCase):
    auto_create_board = True
    auto_create_lists = True

    def test_hello_world(self):
        result = hello_world()
        self.assertEqual(result, "Hello World")
```

The default Board name is "Tresto" with 'PASSED' and 'FAILED' as list names.

In these examples, the `hello_world` function returns "Hello World", and the `TestHelloWorld` class inherits from `TrestoTestCase` and contains a single test case that asserts that the result of calling `hello_world` is equal to "Hello World".

When you run this test, Tresto will create a Trello card with the name of the test and move it to the "IN PROGRESS" list. After the test finishes running, the card will be moved to either the "TEST PASSED" or "TEST FAILED" list, depending on the test result.

## Contributing

Contributions are welcome! If you have an idea for a new feature or want to fix a bug, please submit a pull request.

## License

Tresto is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

Tresto is built using the [py-trello](https://github.com/sarumont/py-trello) library. Thank you to the py-trello developers for their great work!
