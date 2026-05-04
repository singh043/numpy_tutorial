import numpy as np

# Creating Arrays

# arr = [1, 2, 4, 3]

# print(arr * 3)

# np_arr1 = np.array(1)

# print(np_arr1)

# np_arr = np.array([1, 2, 3, 4])

# print(np_arr * 3)

# np_arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# print(np_arr2 * 3)

# np_arr3 = np.array(
#     [
#         [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
#         [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
#         [
#             [19, 20, 21],
#             [22, 23, 24],
#             [25, 26, ""],
#         ],
#     ]
# )

# print(np_arr3)

# Slicing

# array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

# print(array[2])
# print(array[0:3])
# print(array[0, 2])

# print(array[2:, 2:])

# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# print("Last element from 2nd dim: ", arr[1, -1])

# items = [10, 20, 30, 40]
# # print(np.random.choice(items))
# print(np.random.choice(items, size=2, replace=False))

# arr = np.array([10, np.nan, 30])
# # print(np.isnan(arr))
# # print(arr[~np.isnan(arr)])
# print(np.mean(arr))
# print(np.nanmean(arr))
# print(np.nan_to_num(arr, nan=0))
# print(np.where(np.isnan(arr), np.nanmean(arr), arr))


# 1. Array Creation


# arr = np.zeros(5)
# arr = np.zeros((5, 4))
# print(arr)
# arr = np.ones(5)
# arr = np.ones((5, 6))
# print(arr)
# arr = np.full((2, 3), 7)
# print(arr)

# 2. Sequencing

# arr = np.arange(1, 10, 2)
# arr = np.arange(40)
# print(arr)

# 3. Identity matrix

# identity_matrix = np.eye(5)
# print(identity_matrix)

""" Advanced Numpy """

# 4. Insert in array

# arr = np.array([1, 2, 3, 4, 6])
# new_arr = np.insert(arr, 4, 5)
# print(new_arr)

# arr_2d = np.array([[1, 2], [3, 4]])
# new_arr_2d = np.insert(arr_2d, 0, [5, 6], axis=0)
# print(new_arr_2d)
# new_2d = np.insert(arr_2d, 0, [5, 6], axis=1)
# print(new_2d)

# 5. Append in array

# arr = np.array([10, 20, 30])

# new_arr = np.append(arr, [50, 60, 70])

# print(new_arr)

# arr_2d = np.array([[10, 20, 30]])

# new_arr_2d = np.append(arr_2d, [[50, 60, 70]], axis=0)

# print(new_arr_2d)

# 6. Concat array

# arr1 = np.array([[10, 20, 30]])
# arr2 = np.array([[40, 50, 60]])

# new_arr = np.concatenate((arr1, arr2))

# print(new_arr)

# 7. Deleting from array

# arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

# new_arr_2d = np.delete(arr_2d, 0, axis=0)

# print("new_arr_2d", new_arr_2d)

# new_arr_2d = np.delete(arr_2d, 0, axis=1)

# print("new_arr_2d", new_arr_2d)

# 8. Stacking

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])

# print(np.vstack((arr1, arr2)))
# print(np.hstack((arr1, arr2)))

# 9. Split

# arr = np.array([10, 20, 30, 40, 50, 60])

# print(np.split(arr, 6))

# 10. Broadcasting

# prices = np.array([100, 200, 300])

# discount = 10

# final_prices = prices - (prices * discount / 100)

# print(final_prices)


# 11. Handling nan

arr = np.array([1, 2, np.nan, 4, 5, np.nan])

# print(np.isnan(arr))

cleaned_arr = np.nan_to_num(arr)

print(cleaned_arr)

cleaned_arr = np.nan_to_num(arr, nan=100)

print(cleaned_arr)
