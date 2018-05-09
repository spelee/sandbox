import time

def timer(func, *args):
    """Simplistic timing function
    Problems with include:
    1) Hardcodes repetitions count
    2) Charges the cost of the range to the tested function's time
    3) Always uses time.clock, which might not be best outside Windows
    4) Doesn't give callers a way to verify that the tested function actually worked
    5) Only give total time, which my fluctuate on some heavily loaded machines
    6) Doesn't support keyword arguments in the tested function call
    """
    start = time.clock()
    for i in range(1000):
        func(*args)

    return time.clock() - start # elapsed time in seconds


if __name__ == "__main__":
    print(timer(pow, 2, 1000))
    print(timer(str.upper, 'spam'))

