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
        print(f"Duration of function execution is : {end - start : 0.8f} S")
        func_status = False
        return result

    return wrapper


def cache(func):
    my_memory = {}
    func_status = False

    def wrapper(*args, **kwargs):
        nonlocal func_status
        if func_status:
            return func(*args, **kwargs)
        func_status = True
        if args in my_memory:
            print("readed from cache")
            return my_memory[args]
        result = func(*args, **kwargs)
        my_memory[args] = result
        func_status = False
        return result

    return wrapper


@timing_decorator
@cache
def fibo(n):
    if n == 0 or n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)


print(fibo(8))
print("---------------------")
print(fibo(8))
