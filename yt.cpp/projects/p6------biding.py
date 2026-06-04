details={}

def final(persons):
    highest=0
    for i in persons:
        money=persons[i]
        if money>highest:
            highest=money
            winner=i
    print(f"so the winner in the option was-------> {winner}\n whith the highest bid ------->{persons[winner]} \n ------>congratulations<----------")        

stop=False
while not stop:
    name=input("enter the name of the bidder--------->")
    prise=int(input("entr the print the bidder bid----->"))
    details[name]=prise
    v=input("say that is there any bider for the bidding \n---->yes or no<-----\n type----->")
    if v=="no":
        stop=True
s=details
final(persons=s)     
 

          