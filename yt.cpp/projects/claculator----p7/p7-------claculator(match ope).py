def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b!=0:
        return a/b
    else:
        print("invalid")
        return div(a,b)
def claculator():
    stay=False
    a=float(input("enter the 1st vlaue"))
    while not stay:
        operation=input("pick one of the operations\n + \n - \n * \n / \n-------->")
        b=float(input("enter the 2nd vlaue"))

        match operation:
            case "+":
                m=add(a,b)
            case "-":
                m=sub(a,b)
            case "*":
                m=mul(a,b)
            case "/":
                m=div(a,b)
            case _:
                print("invalid option")
        print(f"{a} {operation} {b} = {m}") 
        con=input(f"say that you want to countinue whith vlave-----> {m}\n ------>yes or no<-------- \n or want to exit----->").lower()
        if con=="yes":
          a=m
        elif con=="no":
           claculator()
           return
        elif con=="exit":
          stay=True  
            
claculator()
