a = input("enter the character: ").strip()
b = input("enter the character: ").strip()

if a > b:
    print("a is bigger",a)
elif b > a:
    print("b is bigger",b)
else:
    print("both are equal",a,b)

"""output:
C:\Users\LOKESH\OneDrive\Desktop\pythone PRS program>python -u "c:\Users\LOKESH\OneDrive\Desktop\pythone PRS program\30-5-26\char.py"
enter the character: lokesh
enter the character: kingkong
a is bigger lokesh
"""