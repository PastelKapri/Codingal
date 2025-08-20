def func1(n):
    return n*(n+1)/2
print("function 1 \n" ,func1(77))

def func2(n):
    sum = 0
    for i in range(n+1):
        sum+=1
    return sum
print("function 2 \n" ,func2(4))

def func3(n):
    sum = 0
    for i in range(n+1):
        for j in range(n+1):
            sum+=1
    return sum
print("function 3 \n" ,func3(4))