from math import sqrt

'''num = int(input("Enter a number: "))

if num > 1:
    for i in range(2,int(sqrt(num))+1):
        if num % i == 0:
            print(num, "is not a prime number")
            break
        else:
            print(num, "is a prime number")
            break
else:
    print(num, "is not a prime number")'''


'''def primeseive(n):
    prime = [True for i in range(n+1)]
    currentnum = 2
    while(currentnum * currentnum <= n):
        if(prime[currentnum]):
            for i in range(currentnum**2, n+1, currentnum):
                prime[i] = False
        currentnum += 1
    prime[0] = prime[1] = False
    for p in range(n+1):
        if(prime[p]):
            print(p)

n = int(input("Enter a number to find all the primes of the number: "))
primeseive(n)'''


a = 3000
for num in range(1, a+1):
    c = 0
    temp = num 
    for i in range(1,temp+1):
        if temp % i ==0:
            c+=1
    if c == 2:
        rev = 0
        t = num
        while t > 0:
            rev= rev*10 + (t%10)
            t//=10
        print("palindrome prime \n")
        if rev == num:
            print(num)