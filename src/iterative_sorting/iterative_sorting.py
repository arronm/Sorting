### Algorithm
# 1. Start with current index = 0

# 2. For all indices EXCEPT the last index:

#     a. Loop through elements on right-hand-side 
#     of current index and find the smallest element

#     b. Swap the element at current index with the
#     smallest element found in above loop


# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # TO-DO: swap

    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swapped = 1
    iterations = 0
    while swapped > 0:
        swapped = 0
        for index, item in enumerate(arr, start=0):
            iterations += 1
            if index >= len(arr) - 1:
                break
            if arr[index] > arr[index + 1]:
                swapped += 1
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
    print(f"{iterations} iterations")
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

# unsorted = [4, 2, 3, 1, 5]
# sorted = selection_sort(unsorted)
# print(sorted)