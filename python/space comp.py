"""def prints(n):
    if n<=0:
        return
    print(n/2)
prints(5)

def sum(n):
    return n * (n + 1) // 2

def arraysum(a):
    total = 0
    for i in a:
        total += i
    return total
a = [12,3,4,15]

arraysum(a)

def summ(n):
    if n <=0:
        return 0
    return n + summ(n-1)"""


def BinarySearch(arr,target,low,high):
    if low > high:
        return -1  # Target not found
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return BinarySearch(arr, target, low, mid - 1)
    else:
        return BinarySearch(arr, target, mid + 1, high)

def binary_search(arr, target):
    return BinarySearch(arr, target, 0, len(arr) - 1)

if __name__ == "__main__":

    sorted_array = [2,5,8,12,16,23,38,45,56,72,91]
    target = 16
    result = binary_search(arr, target)

    if result != -1:
        print(f"Target {target} found at index {result}")
    else:
        print(f"Target {target} not found in the array")
