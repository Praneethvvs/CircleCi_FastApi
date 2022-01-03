import time
import traceback
import cProfile, pstats, io

class Time_Detector():

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        start_time = time.perf_counter()
        result = self.original_function(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Time consumed to execute the program is {round(end_time - start_time, 2)} secs")
        return result


def exception_handler(func):
    def sub_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            traceback.print_exc()
            print("Failed to establish connection, Please check the query again.")

    return sub_function





def profile(fnc):
    """A decorator that uses cProfile to profile a function"""

    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner