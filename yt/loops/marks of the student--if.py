x = eval(input("enter the makes of the student:"))

if (x >= 0):
    if (x >= 90 and x <= 100):
        print("A grade")
    elif (x >= 70 and x < 90):
        print("B grade")
    elif (x >= 35 and x < 70):
        print("c grade") 
    else:
        print("fail:")
else:
    print("invalid marks")
