import time
from functools import wraps


def time_this(func):
    """
    Decorator that reports the execution time
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@time_this
def count_down(n: int):
    """
    count
    :param n:
    :return:
    """
    while n > 0:
        time.sleep(0.5)
        n -= 1


if __name__ == "__main__":
    num = input("num: ")
    count_down(int(num))
