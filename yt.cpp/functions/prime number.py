def prime(n):
    is_prime=True
    for i in range(2,n):
        if n%i==0:
            is_prime=False
    if is_prime==True:
        print("is a prime number")
    else:
        print("is not a prime number")

n=eval(input("enter the number"))
prime(n)        
