import time


def work_time(func_to_decorate):
    """Calculates function run time"""
    def wrapper(*args):
        start_time = time.time()
        func_to_decorate(*args)
        print(f'Время выполнения операции: {time.time() - start_time}\n')
    return wrapper


@work_time
def addition(a, b):
    print(a + b)


print(addition(2, 2))
