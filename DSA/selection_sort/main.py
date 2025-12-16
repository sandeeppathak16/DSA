def selection(arr):
    for i in range(len(arr)):
        small = i

        for j in range(i + 1, len(arr)):
            if arr[small] > arr[j]:
                small = j
        arr[i], arr[small] = arr[small], arr[i]


a = [12, 11, 13, 5, 6]
selection(a)
print(a)
