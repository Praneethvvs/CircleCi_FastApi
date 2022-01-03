# import itertools
#
#
# a = [("Animal",1),("Animal",2),("Person",2),("Parson",3)]
#
# x = {key:list(values) for key,values in itertools.groupby(a, lambda x:x[0][:2])}
#
# print(x)


import string

# def my_fun(inp):
#     assert int(inp)>0, "Provide a number greater than 0"
#     alpha_list = list(string.ascii_uppercase)
#     while int(inp)>26:
#         inp =str(sum(map(int, iter(inp))))
#     return alpha_list[int(inp)-1]
#
# inp = input()
# print(my_fun(inp))

