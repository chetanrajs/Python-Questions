class A:
    def method_A(self):
        print("Method A")
        
class B:
    def method_B(self):
        print("Method B")
        
class C(A,B):
    def method_C(self):
        print("Method C")
        
c = C()
c.method_A()
c.method_B()
c.method_C()
