class stu:
    def dispalt(self,name,marks):
        self.name=name
        self.marks=int(input(f"enter the marks{marks}"))
        print(f"you have enter the marks-->{marks} and you name is-->{name}")
    def display(self,sa):
            
            if(self.marks>=35):
                print(f"your pass and your mars r{self.marks} and {sa}")
            else:
                print(f"your pass and your mars r{self.marks} and {sa}")
            
s=stu()
s.dispalt("lokesh",36)
s.display(35)