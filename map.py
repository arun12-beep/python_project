#using lambda function

lst=[1,2,3,5,6,7,8,9]
squares=list(map(lambda x:x**2,lst))
print("square numbers are:",squares)

#using normal function

def square(num):
    return num**2
lst=[1,3,5,6,7,8,9]
squares=list(map(square,lst))
print("square numbers:",squares)