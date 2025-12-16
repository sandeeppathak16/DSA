def bubble_sort(list):
    l = len(list)

    for i in range(l - 1):
        flag = 0
        for j in range(l - i - 1):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
                flag = 1
        if flag == 0:
            break


l = [12, 4, 6, 123, 123, 33, 8]
bubble_sort(l)
print(l)
