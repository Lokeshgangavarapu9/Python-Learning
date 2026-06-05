import random
import p8

def diffculity(v):
    if v=="eazy":
        attements=10
        print(f"number between 1 to 50 and you have only {attements} chances to finish the challange")
        answer=random.randint(1,50)
        return attements,answer
    elif v=="hard":
        attements=15
        print(f"number between 1 to 100 and you have only {attements} chances to finish the challange")
        answer=random.randint(1,100)
        return attements,answer
    elif v=="pro":
        attements=20
        print(f"number between 1 to 250 and you have only {attements} chances to finish the challange")
        answer=random.randint(1,250)
        return attements,answer

def check_answer(attements,guess,answer):
    if(guess>answer):
        print("your guess is too high")
        attements-=1
        print(f"you have only {attements} remaning")
        return attements
    elif(guess<answer):
        print("your guess is too low")
        attements-=1
        print(f"you have only {attements} remaning")
        return attements
    elif guess==answer:
        
        attements=-1
        return attements


print(p8.logo)
v=input("enter te diffculity level\n -------->eazy or hard or pro <---------").lower()
attements,answer=diffculity(v=v)
print(answer)
print(f"you have {attements} attements to finish the challange")
stop=False
while not stop:
    guess=int(input("enter your number---->"))
    attements=check_answer(attements,guess,answer)
    if attements==0:
        print(f"you lost the game\n you fail to guess the number\n-------->the number was {answer}<---------")
        stop=True
    elif attements==-1:
        print(f"{guess} = {answer} \n---------->congratulation your answer was correct<-----------")
        stop=True


