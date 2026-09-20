

def binary_search(arr, item):
    low = 0 #  we starts witrh this at the 0 index for the array
    high = len(arr) - 1 # this starts at the final of the last value for the array 


    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        
        if item == guess:
            return mid
        # If the guess is too low the low accordingly
        elif guess < item: 
            low = mid + 1
        else:
            high = mid - 1

    return None


lista = [1,3,8,9,10]

print(binary_search(lista, 8))
print(binary_search(lista, -3))