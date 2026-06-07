class car:
    
    def input(self):
      self.colour=input("enter the colour you want")
      self.prise=int(input("enter the prise of the car you need"))
    def display(self):
        print(f"colour of the csr is----> {self.colour} /n and prise is {self.prise}")

car_1=car()
car_2=car()
car_1.input()
car_2.input()
car_1.display()
car_2.display()
