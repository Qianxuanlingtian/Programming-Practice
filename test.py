class A:
    x = 250
    def __init__(self, x):
        self.x = x
        
class B:
    x = 520
    def __init__(self, x):
        self.x = x

class C(A):
    c = 10
    def __init__(self, x, c):
        super().__init__(x)
        self.c = c

class D(B):
    def __init__(self, x, d):
        super().__init__(x)
        self.d = d

class E(C, D):
    pass
