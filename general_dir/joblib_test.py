import os

from joblib import Parallel, delayed
import time

print(os.cpu_count())


class Time_Detector():

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        start_time = time.perf_counter()
        result = self.original_function(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Time consumed to execute the program is {round(end_time - start_time, 2)} secs")
        return result


def generate_cubes_list(inp):
    return [i ** 3 for i in range(inp)]


@Time_Detector
def main(type_of_processing, no_of_workers):
    results = Parallel(n_jobs=no_of_workers, backend=type_of_processing)(map(
        delayed(generate_cubes_list), [1000, 100000000, 1500000]))
    return list(map(len, results))


if __name__ == "__main__":
    type_of_processing = "threading" #use this for threading
    type_of_processing = "multiprocessing" #use this for multiprocessing
    no_of_workers = 3  #change this value to set the number of threads or processes
    print(main(type_of_processing, no_of_workers))