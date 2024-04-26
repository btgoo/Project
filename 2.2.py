def uppercase_decorator(func):
    def wrapper(name):
        result = func(name)
        return result.lower()
    return wrapper

@uppercase_decorator
def greet(name):
    return f"Hello, {name}!"

name_input = input("Name:")
result = greet(name_input)
print(result)