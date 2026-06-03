k=(input("enter the vlaue of k: "))
m=(input("enter the value of m: "))
print("before swapping k and m is: " + str(k) + " and " + str(m))
temp=k
k=m
m=temp

k,m=temp,k

print(k)
print(m)
print(temp)
print(type(k))
print(type(m))
print(type(temp))