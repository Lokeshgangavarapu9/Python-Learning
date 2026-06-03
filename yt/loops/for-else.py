numbers=[]

k=int(input("enter the noof values want tobe enter"))

for i in range(k):
    num=int(input(f"the numbers r {i+1}-------->"))
    numbers.append(num)
    print(numbers)
else:
    for c in numbers:
       if c%2==0:
        print(f"the even numbers are---->{c}")
       else:
        print(f"odd numbers r----->{c}")
    else:
       print("program was excutited")
       print(f"total output is the\n nof values you choose------->{k}\nnumbers--->{numbers}\n even and odd numbers r ---->{c}")