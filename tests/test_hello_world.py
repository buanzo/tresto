from tresto import TrestoTestCase

def hello_world():
    return "Hello World"

class TestHelloWorld(TrestoTestCase):
    auto_create_board = True
    auto_create_lists = True

    def test_hello_world(self):
        result = hello_world()
        self.assertEqual(result, "Hello World")
