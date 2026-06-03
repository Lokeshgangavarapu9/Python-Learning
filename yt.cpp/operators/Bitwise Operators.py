#Bitwise Operators
a=5
b=4 
#bitwise and operator --> is used to compare each bit of two numbers and return 1 if both bits are 1 otherwise return 0
print(a&b)

#bitwise or operator --> is used to compare each bit of two numbers and return 1 if at least one bit is 1 otherwise return 0
print(a|b)

#bitwise xor operator --> is used to compare each bit of two numbers and return 1 if both bits are different otherwise return 0
print(a^b)

#bitwise not operator --> is used to reverse the bits of a number
print(~a)

#bitwise left shift operator --> is used to shift the bits of a number to the left by a specified number of positions
#formula=a<<n --> a*(2**n)
print(a<<2)

#bitwise right shift operator --> is used to shift the bits of a number to the right by a specified number of positions
#formula=a>>n --> a//(2**n)
print(a>>2)

