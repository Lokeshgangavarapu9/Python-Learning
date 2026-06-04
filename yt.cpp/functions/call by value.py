def callby_value(num):
    print(f"in the function before change{num}")
    num+=10
    print(f"in the function after change{num}")

x=10
z=callby_value(x)
print(f"out side the function {x}")
