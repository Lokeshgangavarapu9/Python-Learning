import random
import hangma_stages

list=["king","kong","smile","silly"]
k=random.choice(list)


lifes=6
display=[]
for i in range(len(k)):
    display+='-'
print(display)
while lifes > 0 and '-' in display:
     user=input("enter the letter you r gessing").lower()
     for postion in range(len(k)):
        letter=k[postion]
        if letter==user:
            display[postion]=letter
     print(display)
     if user not in k:
        lifes-=1
        print(f"you have enterd the wrong letter \n remening lifes r {lifes}")  
        print(hangma_stages.stages[lifes])     

if '-' not in display:
    print("------------you have wnon-------------")
else:
    print("-----------you have lost-------------")