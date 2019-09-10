# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    indexA = 0
    indexB = 0

    for i in range(len(merged_arr)):
        if arrA[indexA] <= arrB[indexB]:
            merged_arr[i] = arrA[indexA]
            indexA += 1
        else:
            merged_arr[i] = arrB[indexB]
            indexB += 1
        if indexB == len(arrB):
            # Append last element in arrB
            merged_arr = [*merged_arr[:i + 1], *arrA[indexA:]]
            break
        elif indexA == len(arrA):
            # Append last element in arrA
            merged_arr = [*merged_arr[:i + 1], *arrB[indexB:]]
            break

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # Base case we have one element
    if len(arr) <= 1:
      return arr

    # Otherwise keep splitting the array until we get two elements
    # Find the middle of the array
    mid_index = len(arr) // 2

    # Merge sort each half
    return merge(merge_sort(arr[:mid_index]), merge_sort(arr[mid_index:]))

    # return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
