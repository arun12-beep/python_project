set1=set()     #we have to user set() constructor to initialize an empty sets. if we write '{}' python treats it as dict not set.
set2=set()
num=int(input("how many elements you want in set"))
print("enter elements in set1:")
for i in range(1,num+1):
    n=int(input(f"enter num{i}:"))
    set1.add(n)
print("enter elements in set2:")
for i in range(1,num+1):
    n=int(input(f"enter num{i}:"))
    set2.add(n)
print("set1:",set1)
print("set2:",set2)
intersection=set1.intersection(set2)
union=set1.union(set2)
difference=set1.difference(set2)
print("union of sets is:",union)
print("difference of sets is:",difference)
print("intersection of sets is:",intersection)


