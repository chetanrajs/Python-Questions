class A:
    def method_A(self):
        print("Method A")
        
class B(A):
    def method_B(self):
        print("Method B")
        
class C(A):
    def method_C(self):
        print("Method C")
        
class D(B,C):
    def method_D(self):
        print("Method D")
        
d = D()
d.method_A()
d.method_B()
d.method_C()
d.method_D()
