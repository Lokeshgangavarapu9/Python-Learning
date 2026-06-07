class a:
    
    def suma(self):
        self.e=int(input("eter the value of c in a"))
        self.b=int(input("enter the vlaue of b"))
        self.sum=self.e+self.b
        print(self.sum)

class b(a):  

    def sub(self):
        self.c=int(input("eter the value of c in a"))
        self.d=int(input("enter the vlaue of b"))
        self.diff=self.c-self.d
        print(self.diff)

class c(a):
    def mul(self):
        self.c=int(input("eter the value of c in a"))
        self.g=int(input("enter the vlaue of b"))
        self.mu=self.c*self.g
        print(self.mu)
class z(b,c):
    def display(self):
        print(f"{self.mu} and {self.diff} and {self.sum}")

y=z()
y.display 
y.suma()
y.sub()
y.mul()       


