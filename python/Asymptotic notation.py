def printnum(n): #Constant time complexity O(1) Best case
    print(f"number entered is {n}")
    print("iterations are 1")

printnum(5)
printnum(10)
printnum(15000)
printnum(1000000)

def ontime(n): #Linear time complexity O(n) Average case
    for i in range(1,n+1):
        print("iteration", i)
    print("num of iterations is", n)

ontime(5)
ontime(10)
ontime(20)

def onsquaeredtime(n): #Quadratic time complexity O(n^2) Worst case
    interations = 0
    for i in range(n):
        for j in range(n):
            interations += 1
            print(f"iteration is {interations}: i is {i} and j is {j}")
    print("num of iterations is", interations)


onsquaeredtime(2)
onsquaeredtime(3)
onsquaeredtime(5)