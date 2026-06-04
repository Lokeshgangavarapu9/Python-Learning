def callby_reference(num):
     print(f"in the function before change{num}")
     num.append(99)
     print(f"in the function before change{num}")

num=[1,2,3,5]
callby_reference(num)
print(f"in the function before change{num}")
