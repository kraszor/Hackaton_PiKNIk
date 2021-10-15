import time


def time_measure(func):
    def inside(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        timer = end - start
        info = f'Time elapsed: {timer*1000} ms'
        return info
    return inside
