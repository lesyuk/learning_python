import time


def work_time(func_to_decorate):
    """Calculates function run time"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func_to_decorate(*args, **kwargs)
        print(f'Время выполнения операции: {time.time() - start_time}.\n')
    return wrapper


# Function work example
if __name__ == '__main__':
    @work_time
    def addition(a, b):
        print(a + b)

    addition(2, 2)
