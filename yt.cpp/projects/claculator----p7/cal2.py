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

ope={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}

def calculator():
    stay=False
    a=float(input("enter the vlaue of 1st number--------->"))
    while not stay:
      for i in ope:
        print(i)
      v=input("choose one operation--->") 
      b=float(input("enter the 2nd number------>")) 
      m=ope[v]
      c=m(a,b)
      print(c) 
      print(f"{a} {v} {b} = {c}")
      con=input(f"say that you want to countinue whith vlave-----> {c}\n ------>yes or no<-------- \n or want to exit----->").lower()
      if con=="yes":
          a=c
      elif con=="no":
          calculator()
          return
      elif con=="exit":
          stay=True


calculator()      