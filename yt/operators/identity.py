#Identity Operators
a=5
b=6
#is operator --> is used to check if two variables point to the same object in memory
print(a is b) # True

#is not operator --> is used to check if two variables do not point to the same object in memory
print(a is not b) # False

"""In Python, small integers (from -5 to 256) are cached and reused, so a and b point to 
the same memory location. For larger integers or other data types, this may not be the case."""
print(id(a)) # memory address of a
print(id(b)) # memory address of b
