# a = 2
# b = 6
# a, b = 5, a+6
# print(a, b)

arr = [43,12,23,344,5,9]
print(arr)
def bubble_sort(arr):
    n = len( arr )
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

result = bubble_sort(arr)
print(result)