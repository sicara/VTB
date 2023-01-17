"""Hello world example to show some best coding and testing practices"""


def hello_world() -> None:
    """Says hello to the world"""

    print("Hello, world")


def add_to_one(x: int) -> int:
    """Add one to an integer"""

    return x + 1


def reverse_string(s: str) -> str:
    """Reverse a string"""

    return s[::-1]


def hello_python() -> None:
    """Says hello to the python"""

    print("Hello, Python!")


def add_five_and_two() -> None:
    """Add 5 and 2"""

    print(add_to_one(5) + add_to_one(2))


def reverse_string_python() -> None:
    """Reverse a string"""

    print(reverse_string("Hello, Python!"))


def hello_hello_world_python() -> None:
    """Says hello to hello to the python"""

    print("Hello, Python!")


def not_a_function() -> None:
    """A function that is not a function"""

    hello_world()


def not_a_function_python() -> None:

    print("Hello World!")
