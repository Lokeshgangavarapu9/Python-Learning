size=eval(input("enter the size of the pizza:\n press-1 for small\n press-2 fro the medium\n press-3 for the large\n"))
piza=0
if(size==1):
    print("you have selected the small pizza")
    piza+=150
elif(size==2):
    print("you have selected the medium pizza")
    piza+=250
elif(size==3):
    print("you have selected the large pizza")
    piza+=350
else:
    print("invalid option")

    
pepperoni=eval(input("do you want to add the pepperoni: \n press-1 for the yes \n press-2 for the no \n"))
     
if(pepperoni==1):
        if(size==1):
            piza+=30
        elif(size==2):
            piza+=50
        elif(size==3):
            piza+=70
else:
        print("you have selected no pepperoni")

extra_cheese=eval(input("do you want to add the extra cheese: \n press-1 for the yes \n press-2 for the no \n"))
if(extra_cheese==1):
        piza+=20
else:  
      print("you have selected no extra cheese")



print("the total price of the pizza is:", piza)
