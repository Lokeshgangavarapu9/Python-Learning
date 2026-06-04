import random
k=input("choose head or tail-->").strip().lower()
n=random.randint(0,1)

if (n==1):
    computer="head"
    
else:
    computer="tail"

print(f"toss is -->{computer}")

if(k!="head" and k!="tail"):
    print("invalid option"+"try again")
else:
    print(f"your oiption is {k}")

    
if(k==computer):
    print("you have won✌️")
else:
    print("compurtr has won💻")
