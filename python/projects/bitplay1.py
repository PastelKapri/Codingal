def findsetbit(n):
    if n ==0:
        print("no set bits in 0 :)")
    else:
        pos =1
        while (n&1)==0:
            n>>=1
            pos+=1
        print(f"the rightmost set bit is at position {pos}")
n = int(input("Enter a number: "))
findsetbit(n)