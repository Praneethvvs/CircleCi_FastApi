import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import requests
import time

url = "https://httpbin.org/uuid"

class Time_Detector():

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        start_time = time.perf_counter()
        result = self.original_function(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Time consumed to execute the program is {round(end_time - start_time, 2)} secs")
        return result


def generate_squares_list(inp):
    return [i for i in range(inp)]


def fetch(session, url):
    with session.get(url) as response:
        print(response.json()["uuid"])

@Time_Detector
def main():
    with ProcessPoolExecutor(max_workers=3) as executor:

        # I/O bound task
        # with requests.Session() as session:
        #     arg_list = [(session,url)]*100
        #     executor.map(fetch, *(zip(*arg_list)))
        #     executor.shutdown(wait=True)

        # cpu_bound_task
        results = executor.map(generate_squares_list,[1000,100000000,1500000])
        executor.shutdown(wait=True)
        return list(map(len,results))


# print(os.cpu_count())

if __name__ == "__main__":
    print(main())
