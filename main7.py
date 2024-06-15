# Напишите программу, которая создает двумерный массив размером 3x3 и заполняет его числами от 1 до 9.
# Затем программа должна выводить строку из элементов каждой строки массива.

A = [
    [1,2],
    [4,5]
]
B = [
    [7,8],
    [9,1]
]

# def mult_matrix(A,B)
#     C = []
#     for i in range(2):
#         for j in range(2):
#             # A[i][i]*B[i][j]
# https://thecode.media/wp-content/uploads/2021/03/11.jpg
# matrix = [
#     [2,6],
#     [3,7],
#     [4,8],
#     [5,9]
# ]
#
# def transpose_matrix(matrix):
#     n = len(matrix)
#     transposed = [[0]*n for _ in range(n)]
#     for i in range(n):
#         for j in range(len(matrix[i])):
#             transposed[j][i] = matrix[i][j]
#     return transposed
#
# print(transpose_matrix(matrix))
#
#
#
# transpose_matrix(matrix)
# numbers = []
# num = 1
# for i in range(3):
#     numbers.append([])
#     for j in range(3):
#         numbers[i].append(num)
#         num += 1
#
# result = ""
# for i in range(len(numbers)):
#     for j in range(len(numbers[i])):
#         result += str(numbers[i][j])
#
# print(result)
# nums = [
#     [32,45],
#     [2,5,1],
#     [8,62,5]
# ]
#
# max = 0
# for i in range(len(nums)):
#     for j in range(len(nums[i])):
#         if max < nums[i][j]:
#             max = nums[i][j]
#
# print(max)

#
# sum = 0
# countInteration = 0
# for i in range(len(nums)):
#     for j in range(len(nums[i])):
#         sum += nums[i][j]
#         countInteration += 1
# print(sum/countInteration)

# result = []
# def calc(t):
#     result.append([2*t**3, 6*t**2, 4*t])
#
# for i in range(11):
#     calc(i)
#
# for i in range(len(result)):
#     print(f"При t={i}с S={result[i][0]}; V={result[i][1]}; a={result[i][2]}")










#arr = [43,12,23,344,5,9]

#print(sorted(arr))

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)


# arr2 = [x for x in arr if x%2==0]
#
# for i in range(len(arr)):
#     if arr[i]%2==0:
#         arr2.append(arr[i])
#
# print(arr2)