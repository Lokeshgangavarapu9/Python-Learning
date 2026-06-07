class phone:
    def input(self,brand):
        self.model=input(f"enter the model of the {brand}")
        self.problem=input("whats your problem")
        self.brand=brand
    def output(self):
        print(f"sending this request to {self.brand} company")    

class company(phone):
    def replay(self):
        print(f"we have seen your request of {self.model}")  

c=company()
c.input("samsung")
c.output()
c.replay()

