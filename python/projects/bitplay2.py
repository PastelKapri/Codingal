n = int(input("Enter a number: "))

bit_length = n.bit_length()

reversed_num = 0

for i in range(bit_length):
    reversed_num = (reversed_num << 1) | (n & 1)
    n >>= 1

print("Reversed number:", reversed_num)