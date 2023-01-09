def binarysearch(massive, item):
    low = 0
    high = len(massive) - 1
    i = 0
    while low <= high:
        mid = (low + high) // 2
        guess = massive[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
        i=i+1
        print(i)
    return None

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 35, 39, 42, 45, 48, 51, 55, 57, 59, 62, 65, 69, 71, 75, 79, 81, 83, 86, 89, 92, 94, 99, 101]
print(binarysearch(testlist, 3))
