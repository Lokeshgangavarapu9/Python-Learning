#floor division operator(//)
print(5/2)
print(4/2)
print(4//2) # is floor division operator(//)
print(5//2) # is floor division operator(//)

#power operator(**)
print(2**3) # 2*2*2

#operators precendence

#  bracket > power > exponentiation > multiplication > division > addition > subtraction
#   ()     > **    > * , / , // > + , -

#associativity of operators
#  left to right > right to left
#power operator(**)--> is right to left associative(R-->L)
#(* , / , // > + , -)--> are left to right associative(L-->R)

#example of associativity of operators
print(2**3**2) # 2**(3**2)--> 2**9-->512
print(((2**3)**2)) # ((2**3)**2)--> (8**2)-->64
