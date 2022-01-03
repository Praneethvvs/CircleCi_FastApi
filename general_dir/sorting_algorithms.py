from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def myfun(self):
        return 1


    def testfun(self):
        print(1)
class C(A):
    pass

C().testfun()