print("-" * 15)
print("Task1:")


def deco_1(func):
    def wrapper(*args, **kwargs):
        print(
            f"Calling a function: {func.__name__} with args: {args} and kwargs:{kwargs}"
        )
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result

    return wrapper


@deco_1
def func_1(x, y):
    return x * y


print("Result: ", func_1(22, 7))

# -----------------------------------------------------------------------------

print("-" * 15)
print("Task2:")

import time


def deco_2(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("Time spent: ", t2 - t1)
        return result

    return wrapper


@deco_2
def func_2():
    print("I will count to 10.000!")
    ctr = 0
    while ctr < 10000:
        ctr += 1
    print("I did it!!!")
    return True


func_2()


# -----------------------------------------------------------------------------

print("-" * 15)
print("Task3:")


def deco_3(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(
            f"I will transform return value of {func.__name__} from {type(result)} to list"
        )
        print(f"Function return is: {result}")
        result = [result]
        print(f"Check it now: {type(result)}, and the output is: {result}")
        return result

    return wrapper


@deco_3
def func_3():
    return "Is there life on Mars?"


func_3()

# -----------------------------------------------------------------------------

print("-" * 15)
print("Task4:")


def deco_4(condition):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition(*args, **kwargs):
                return func(*args, **kwargs)
            else:
                raise ValueError("Invalid arguments passed to the function")

        return wrapper

    return decorator


@deco_4(lambda x: x > 0)
def func_4(x):
    return x**3


print(func_4(5))  # Output: 125
# print(func_4(-2))  # Raises ValueError: Invalid arguments passed to the function

# -----------------------------------------------------------------------------

print("-" * 15)
print("Task5:")


def deco_5(default_response):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Exception occured: {e}")
                return default_response

        return wrapper

    return decorator


@deco_5(default_response="An error occured!")
def func_5(x, y):
    return x / y


result = func_5(22, 0)
print("Result: ", result)
