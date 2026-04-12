lst=[x for x in range(1,16)]
even_count=0
odd_count=0
for n in lst:
    if n%2==0:
        even_count+=1
    else:
        odd_count+=1
print("list elements:",lst)
print("even count:",even_count)
print("odd count:",odd_count)