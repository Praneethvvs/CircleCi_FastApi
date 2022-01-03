# class A():
#     def square(self):
#         print(self.a ** 2)
#
#
# class B(A):
#
#     def cube_and_square(self,num):
#         print(num ** 3)
#         self.a = num
#         super().square()
#
#
# B().cube_and_square(5)


# class Node1():
#     def __init__(self):
#         print("node1")
#
# class Node2(Node1):
#     def __init__(self):
#         print("node2")
#         super(Node2, self).__init__()
#
# class Node3(Node1):
#     def __init__(self):
#         print("node3")
#         super(Node3, self).__init__()
#
# class Node4(Node3,Node2):
#     def __init__(self):
#         print("node4")
#         super(Node4, self).__init__()
# from pprint import pprint
# pprint(Node4.mro())
from pprint import pprint
import pandas as pd
from collections import Counter
df = pd.read_excel("G&C Corpus_new.xlsx",sheet_name="Convenience")["Convenience Name"]
df2 = pd.read_excel("G&C Corpus_new.xlsx",sheet_name="Fuel")["Fuel Name"]

pprint(sum(1 for k,v in Counter(list(df)+list(df2)).items() if v==2))













