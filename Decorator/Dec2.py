import time


def timing_decorator(func):
    func_status = False

    def wrapper(*args, **kwargs):
        nonlocal func_status
        if func_status:
            return func(*args, **kwargs)
        func_status = True
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{end - start : 0.6f} S")
        func_status = False
        return result

    return wrapper


@timing_decorator
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


x = factorial(3)
print(x)
