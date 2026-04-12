lst=input("enter list elements separated by spaces").split()
lst_org=list(map(int,lst))            # split() method creates a list of string so we are converting string of list to int using map(int,lst)
first=second=float('-inf')
for num in lst_org:
    if num>first:
        second=first
        first=num
    elif num>second and num!=first:
        second=num
print(f"largest number is {first}")
print(f"second largest number is: {second}")






'''
if num>first
  second=first
  first=num
elif num>second and num!=first
  second=num
'''