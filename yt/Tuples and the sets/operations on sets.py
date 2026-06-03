#1.union
#2.intersection
#3.symetric difference

set1={1,23.5,True,"hellow"}
set2={1,24.5,False,"hellow"}
set3={"panipuri",34,34.555,23}


#union------------------------------------>

m=(set1.union(set2,set3))
print(m)
print(set1 | set2 | set3)
print(set1.union(("kinkkong",56,56.3)))
k=set1.update(set2)
set1.update(("simba",345))
print(set1)
print(set1 and set2)

#intersection------------------------------------------->

f=set1.intersection(set2,set3)
print(f)
print(set1.intersection(["hellow",23]))
set1.intersection_update(set2)
print(set1)

#symmetric differecce---------------------------->

set1.difference(set2)
print(set1)
