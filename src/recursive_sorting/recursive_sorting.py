# TO-DO: complete the helpe function below to merge 2 sorted arrays
arr1 = [1, 3, 5]
arr2 = [2, 4, 6, 40, 60, 600, 10000]
arr3 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]


def merge(arrA, arrB):
    # print(f"ArrayA: {arrA}")
    # print(f"ArrayB: {arrB}")
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    # create variables for the indexes of arrA, arrB, and merged_arr
    # k is the index of the merged_arr that we will be adding a value to, i is the current index we are examining in arrA, and j is the current index in arrB
    i = 0
    j = 0
    k = 0
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            k += 1
            i += 1
        else:
            merged_arr[k] = arrB[j]
            k += 1
            j += 1

    while i < len(arrA):
        merged_arr[k] = arrA[i]
        k += 1
        i += 1

    while j < len(arrB):
        merged_arr[k] = arrB[j]
        k += 1
        j += 1
    return merged_arr


# print(merge(arr1, arr2))
# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        middle = len(arr) // 2
        left_half = merge_sort(arr[:middle])
        right_half = merge_sort(arr[middle:])
        return merge(left_half, right_half)
    else:
        return arr


print(merge_sort(arr3))
# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
