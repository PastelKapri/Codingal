'''def swap(a,b):
    a=a^b
    b=a^b
    a=a^b
    print(f"Afer swapping \na={a}\nb={b}")
a=int(input("Enter a: "))
b=int(input("Enter b: "))
swap(a,b)

def swap2(c,d):
    c = (c&d)+(c|d)
    d = c +(~d)+1
    c = c + (~d) + 1
    print(f"After swapping \nc={c}\nd={d}")
c=int(input("Enter c: "))
d=int(input("Enter d: "))
swap2(c,d)'''

def divide(ourdividend,ourdivisor):
    sign = -1 if ((ourdividend<0) ^ (ourdivisor<0)) else 1
    ourdividend = abs(ourdividend)
    ourdivisor = abs(ourdivisor)

    quotient = 0
    temp = 0

    for i in range (31, -1, -1):
        if (temp + (ourdivisor << i) <= ourdividend):
            temp += ourdivisor << i
            quotient |= 1 << i
    if sign == -1:
        quotient = -quotient
    return quotient

a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))
print(f"The quotient is {divide(a,b)}")