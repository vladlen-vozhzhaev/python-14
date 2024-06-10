arr = [43,12,23,344,5,9]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        minIndex = i
        for j in range(i+1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
        print(arr)
    return arr

result = selection_sort(arr)
print(result)