def prime(num):
    if num==1 :
        return False
    else:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            return True
lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
primes=list(filter(prime,lst))
print("elemenets in list:",lst)
print("prime numbers are",primes)