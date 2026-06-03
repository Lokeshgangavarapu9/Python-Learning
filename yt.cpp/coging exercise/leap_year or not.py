y=eval(input("enter the input year: "))

if (y%400==0):
    print("the year is a leap year")
elif (y%100==0):
    print("the year is not a leap year")
elif (y%4==0):
    print("the year is a leap year")
else:
    print("the year is not a leap year")
    