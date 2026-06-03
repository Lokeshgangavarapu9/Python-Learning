"""
Function,What it does
"random.randint(a, b)","Returns a random integer between a and b, including both a and b."
"random.randrange(a, b)","Returns a random integer between a and b, including a but excluding b."
random.random(),Returns a random float between 0.0 and 1.0.
random.choice(seq),"Picks a random element from a list, tuple, or string."
random.shuffle(list),Randomly reorders the elements of a list in place.
"random.uniform(a, b)",Returns a random floating-point number between a and b.
"""
# types of random functions
import random

a=eval(input("Enter the value of a: "))
b=eval(input("Enter the value of b: "))

m=[1,2,3,4,5,6]

random_int=random.randint(a,b)
random_range=random.randrange(a,b)
random_m=random.uniform(a,b)
k=random.choice(m)
s=random.shuffle(m)

print(f"random integer between {a} and {b} is: {random_int}")
print(f"random range between {a} and {b} is {random_range}")
print(f"random float between  is: {random_m}")
print(k)
print(s)

