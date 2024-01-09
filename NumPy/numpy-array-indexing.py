import numpy as np

arr = np.arange(0, 11)
slice_arr = arr[:6]

print(f"\n{arr}\n")

print(f"\narr[8]: \n{arr[8]}")
#8

print(f"\narr[1:5]: \n{arr[1:5]}")
#[1, 2, 3, 4]

print(f"\narr[:6] = arr[0:6]: \n{arr[:6]}")
#[0, 1, 2, 3, 4, 5]

print(f"\narr[5:]: \n{arr[5:]}")
#[5, 6, 7, 8, 9, 10]

arr[:5] = 10
print(f"\narr[:5] = 10: \n{arr}")
#[10, 10, 10, 10, 10, 5, 6, 7, 8, 9, 10]

slice_arr[:] = 99
print("\n\nAfter use slice_arr[:] = 99:")
print(f"\narr: \n{arr}")
#[99, 99, 99, 99, 99, 99, 6, 7, 8, 9, 10]
print(f"\nslice_arr \n{slice_arr}")
#[99, 99, 99, 99, 99, 99]

print("\n\nUsing Copy:")
arr = np.arange(0, 11)
arr_copy = arr.copy()
arr_copy[:] = 13
print(f"\narr: \n{arr}")
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"\ncopy: \n{arr_copy}")
#[13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]


print("\n\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("=-=-=-=-=-=-=-= 2D ARRAYS =-=-=-=-=-=-=-=")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n")

arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

print(arr_2d)
print(f"\nRow 0 (arr_2d[0]): \n{arr_2d[0]}")
print(f"\narr_2d[0][1] \n{arr_2d[0][1]}")
print(f"\narr_2d[0, 1] \n{arr_2d[0, 1]}")

print(f"\narr_2d[:2,1:] \n{arr_2d[:2,1:]}")

print("\n\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("=-=-=-=-=-=-=-=  BOOLEAN  =-=-=-=-=-=-=-=")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n")

arr = np.arange(0, 11)

print(f"\narr > 5: \n{arr > 5}")
print(f"\narr[arr>5] \n{arr[arr>5]}")
print(f"\narr[arr<3] \n{arr[arr<3]}")

print("\n\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("=-=-=-=-=-=-=-= EXERCISE =-=-=-=-=-=-=-=")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n")

arr_2d = np.arange(50).reshape(5, 10)

# [[ 0  1  2  3  4  5  6  7  8  9]
#  [10 11 12 13 14 15 16 17 18 19]
#  [20 21 22 23 24 25 26 27 28 29]
#  [30 31 32 33 34 35 36 37 38 39]
#  [40 41 42 43 44 45 46 47 48 49]]

# Using Slicing, grab 33, 34, 35
print(arr_2d[3, 3:6])

# Using Slicing, grab 16, 17, 18, 26, 27, 28
print("\n\n", arr_2d[1:3, 6:9])