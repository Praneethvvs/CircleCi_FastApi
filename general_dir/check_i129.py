# import json
# from collections import Counter
# from pprint import pprint
#
# a = "123451"
#
# x = dict(map(reversed, enumerate(a)))["1"]
#
#
# print(next(enumerate(a)))

# import time
#
# a = [1,2,1,1,2]
# start_time = time.perf_counter()
# c = sum(map(lambda x: max([index for index,value in enumerate(a,start=1) if value == x]),set(a)))
# end_time = time.perf_counter()
#
# print(c,end_time-start_time)
# start_time = time.perf_counter()
# b = sum(map((lambda x:next(i+1 for i in reversed(range(len(a))) if a[i] == x)),set(a)))
# end_time = time.perf_counter()
# print(b,end_time-start_time)


# def for_mimic(a):
#     b = iter(a)
#     eol = False
#     while not eol:
#         try:
#            c =  next(b)
#         except StopIteration:
#             eol = True
#         else:
#             print (c*5)
#
# for_mimic([1,2,3,4,5])



# print(list(zip(*a))



from datetime import datetime

date = datetime.fromisoformat('2017-01-01T12:30:59.000000')
