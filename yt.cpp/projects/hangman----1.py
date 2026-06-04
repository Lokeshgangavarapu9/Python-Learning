import random
import hangma_stages

word=["apple","kingkong","bananana","cinema"]
k=random.choice(word)
print(k)
display=[]
life=6

for i in range(len(k)):
    display+='-'

print(display)
while(life>0):
    user=input("enter the letter ").lower()
    for postion in range(len(k)):
       letter=k[postion]
       if letter==user:
        display[postion]=user
    print(display)
    if user not in k:
           print("you entered a wrong letter")
           life-=1
           print(f"you having remaning life {life}")
           print(hangma_stages.stages[life]) 
    if '-' not in display:
        life=0
if '-' not in display:
    print(display)
    print("--------you have won---------")
else:
    print("--------game over--------")

