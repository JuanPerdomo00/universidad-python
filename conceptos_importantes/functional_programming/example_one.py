# Funciones normales
def make_upper(text: str) -> str:
    return text.upper()


def make_lower(text: str) -> str:
    return text.lower()


def greet(func, name: str):
    greeting = func(f"Hello, {name}")
    print(greeting)


greet(make_upper, "jakepys")
greet(make_lower, "jakepys")
