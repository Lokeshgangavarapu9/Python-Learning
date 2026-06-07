
pi=3.14

class area:
    def input(self):
        self.l=int(input("enter the lenght of the trrangle"))
        self.b=int(input("ente the breagth of the triang;e"))
        print("------------->circle<---------------")
        self.radius=float(input("enter the radius of the circle"))
    
    def area(self):
        self.s=(float)(self.l*self.b)*1/2
        self.c=2*pi*self.radius


        
    def display(self):
        print(f"area od the triangle of length---->{self.l} and bragth---->{self.b}\n and the read is------>{self.s}")
        print("------------->circle<---------------")
        print(f"radius of the circle----->{self.c}")
a=area()
a.input()
a.area()
a.display()                  