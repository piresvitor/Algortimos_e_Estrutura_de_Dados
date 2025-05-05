def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    steps = 0
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            print ('steps', steps)
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return None

#exemplo de uso
arr0 = [1, 2, 3, 4, 5]
arr1 = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10]
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
target = 3
print(binary_search(arr0, target)) #saida 1
print(binary_search(arr1, target)) #saida 2
print(binary_search(arr2, target)) #saida 3
