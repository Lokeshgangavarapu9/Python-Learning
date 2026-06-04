import random

c=input("what you choose \n rock \n paper \n scissors--->")
print(f"you choose option is---> {c}")
k=random.randint(0,2)

if k==0:
    print("computer choose--> paper🗞️")
    k="paper"
elif k==1:
    print("computer choose--> rock👊")
    k="rock"
else:
    print("computer choose--> scissors✂️")
    k="scissors"

if((c=="rock" and k=="scissors") or (c=="scissors" and k=="paper") or (c=="paper" and k=="rock")):
        print("you r the winner-->✌️🏅")
elif (c==k):
        print("draw-->📍")
else:
      print("computer is the winner-->💻🤙🤘👃")
      