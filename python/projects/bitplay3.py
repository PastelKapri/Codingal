def longestones(n):
    count = 0
    max_count = 0
    
    while n > 0:
        if n & 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
        n >>= 1 
    
    return max_count

num = int(input("Enter a number: "))
print(f"Binary form: {bin(num)[2:]}")
print(f"Longest consecutive 1s: {longestones(num)}")