# چاپ محاسبه زمان اجرای یک تابع با استفاده از دکوریتور
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
        print(f"{end - start: 0.5f} S")
        func_status = False
        return result

    return wrapper


@timing_decorator
def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


x = fibo(15)
print(x)
