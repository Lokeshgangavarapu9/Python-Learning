a=int(input("enter the 1st vlaue"))
b=int(input("enter the 2nd value"))

ch=int(input("press 1.summ , 2.even ,3.odd"))
match ch:
    case 1:
        
          if(a%2==0):
             sum+=a 
             print(sum)
    case 2:
        if a%2!=0:
            sum+=a
            print(sum)         