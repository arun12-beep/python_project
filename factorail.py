
def factorial(*args):
    fact_lst=[]          #declared here so that each function call wouldn't append to fact_lst
    print("passed arguments:",args)
    for arg in args:
        if arg==0 or arg==1:
            fact_lst.append(arg)
        else:
            fact=1
            for i in range(1,arg+1):
                fact=fact*i
            fact_lst.append(fact)
    print("factorials:",fact_lst)
factorial(5,1,3,2)
factorial(9,0)
factorial(7,6,1)


