def sort(array):
    length = len(array)
    for i in range(1, length):
        key = array[i]
        j = i
        while (j - 1 >= 0) and (array[j - 1] > key):
            array[j - 1], array[j] = array[j], array[j - 1]
            j = j - 1
        array[j] = key

arr = [0, 1, 2, 8, 13, 17, 19, 32, 35, 39, 42, 45, 48, 51, 55, 57, 59, 62, 65, 69, 71, 75, 79, 81, 83, 86, 89, 92, 94, 99, 101]
sort(arr)
print("Отсортированный массив: " + str(arr))
