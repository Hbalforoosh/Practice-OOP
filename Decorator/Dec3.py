import time


def timing_decorator(func):
    func_status = False

    def wrapper(*args, **kwargs):
        nonlocal func_status
        if func_status:
            return func(*args, **kwargs)
        func_status = True
        start = time.time()
        result = func(*args, *kwargs)
        end = time.time()
        print(f"Duration of function execution is : {end - start : 0.8f} S")
        func_status = False
        return result

    return wrapper


@timing_decorator
def sum_total(n):
    if n == 1:
        return 1
    return n + sum_total(n - 1)


x = sum_total(5)
print(x)
