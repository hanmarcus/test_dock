import lab1.greet as greet


class TestGreet:
    def test_greet_world(self):
        assert greet.greet("World") == "Hello, World!"

    def test_greet_alice(self):
        assert greet.greet("Alice") == "Hello, Alice!"

    def test_greet_returns_string(self):
        assert isinstance(greet.greet("Bob"), str)

    def test_greet_with_empty_string(self):
        assert greet.greet("") == "Hello, !"

    def test_greet_with_none(self):
        assert greet.greet(None) == "Hello, !"

    def test_greet_with_number(self):
        assert greet.greet(123) == "Hello, 123!"
