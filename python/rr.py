def func1(n):
    if(n <= 0):
        return
    for i in range(0, n+1):
        print("prints")
    func1(n/2)
    func1(n/3)

def func2(n):
    if(n <= 1):
        return
    print("printsr2")
    func2(n-1)

