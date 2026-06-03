n = eval(input("enter the valuve: "))
i = 1
j = 1

# FIXED: Loop runs as long as 'i' is less than or equal to 'n'
while (i <= n):
    if (i % 2 != 0):
        print(i)
    i += 1

while(j <= n):
    if(j%2==0):
        print(j)
    j+=1