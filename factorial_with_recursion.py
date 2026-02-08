def fact(num):
    if num==1:
        return 1
    else:
        factorial=num*fact(num-1)
        return factorial
num=int(input('enter your number'))
print(f" the factorial of the {num}  is : {fact(num)}")    
