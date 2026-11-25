def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest + arr[i]
            smallest_index = i

    return smallest_index

#So we can use this function like a selection sort


def selectionSort(arr):
    newArr =[]

    copiedArr = list(arr)
    for i in range(len(copiedArr)):
        smallest = find_smallest(copiedArr)
        newArr.append(copiedArr.pop(smallest))
    return newArr


print(selectionSort([5, 3, 6, 2, 10]))

