# Binary Search- Iterative

def binary_iter(n, arr):
    start = 0
    stop = len(arr) - 1
    while start <= stop:
        mid = (start + stop) // 2
        if n == arr[mid]:
            return "{} found at index {}".format(n, mid)
        elif n > arr[mid]:
            start = mid + 1
        else:
            stop = mid - 1
    return "{} not found in list".format(n)

def create_list(max_val):
    arr = []
    for num in range(1, max_val + 1):
        arr.append(num)
    return arr

l = create_list(1000)
for num in range(16):
    print (binary_iter(num, l))


# Binary Search- Recursive

def binary_recur(n, arr, start, stop):
    if start > stop:
        return "{} not found in list".format(n)
    else:
        mid = (start + stop) // 2
        if n == arr[mid]:
            return "{} found at index: {}".format(n, mid)
        elif n > arr[mid]:
            return binary_recur(n, arr, mid+1, stop)
        else: 
            return binary_recur(n, arr, start, mid-1)

def create_list(max_val):
    arr = []
    for num in range(1, max_val+1):
        arr.append(num)
    return arr

l = create_list(1000)
for num in range(16):
    print (binary_recur(num, l, 0, len(l)-1))
