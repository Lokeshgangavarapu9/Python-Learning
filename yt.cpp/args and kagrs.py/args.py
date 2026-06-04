def args(*h):
    k = 0
    for i in h:
     print(i)
     k += i
    print(f"sum is {k}")

s=[1,2,3,4] 
m=[12,23,34,45]
args(*s)
args(*m)