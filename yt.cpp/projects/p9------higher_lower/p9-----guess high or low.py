import random
import h
import data_base

points=0
chance=5

print(h.game_logo)
def details(account):
    name=account["name"]
    work=account["description"]
    place=account["country"]
    return (f"name is:{name}\ndescription:{work} \ncountry:{place}")

def compare(followers_1,followers_2,guess):
    if followers_1>followers_2:
        if guess=="high":
            return True
        else:
            return False
    else:
        if guess=="high":
            return False
        else:
            return True
           

life=False  

account_2=random.choice(data_base.data)
while not life : 
    account_1=account_2
    account_2=random.choice(data_base.data)
    while account_1==account_2:
         account_2=random.choice(data_base.data)

    print(f"compare-1:{details(account_1)}")
    print(h.vs)
    print(f"compare-2:{details(account_2)}")

      

    name_1=account_1["name"]
    name_2=account_2["name"]   
    print(f"followers Will {name_1} be HIGHER or LOWER than {name_2}?")
    guess = input("👉 Type 'high' or 'low': ").lower().strip()

    followers_1=account_1["follower_count"]
    followers_2=account_2["follower_count"]
    correct=compare(followers_1,followers_2,guess)

    if correct==True:
        points+=1
        print(f"you guess is correct\n you got------> {points} points")
    elif correct==False:
        chance-=1
        print(f"you guess is wrong\n you have only ------> {chance} chance \n you have totla_points={points} ")
        if chance==0:
            life=True
            print("----------------->GAME OVER<-----------------------")



