# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        
        # TO-DO: find next smallest element
        for j in range (i + 1, len(arr)): # i = 0, j = 1, stop = len(arr)
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

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