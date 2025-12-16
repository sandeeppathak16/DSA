def insertion(arr):
    for i in range(len(arr)):
        small = arr[i]
        j = i - 1
        while j >= 0 and small < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = small


a = [12, 11, 13, 5, 6]
insertion(a)
print(a)
