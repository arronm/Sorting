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
def bubble_sort2( arr ):
    swapped = 1
    iter = 0
    while swapped > 0:
        swapped = 0
        for index in range(0, len(arr) - 1):
            iter += 1
            if arr[index] > arr[index + 1]:
                swapped += 1
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
    print(iter)
    return arr


def bubble_sort3(arr):
    iter = 0
    for i in range(len(arr)):
        # Can assume right side of the array is sorted for every iteration of i
        # no need to check already sorted elements
        for j in range(0, len(arr) - i - 1):
            iter += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(iter)
    return arr


def bubble_sort(arr, idx=1, cur_idx=1, iter=0):
    if cur_idx >= len(arr):
        print(iter)
        return arr
    if idx == 0 or arr[idx] > arr[idx-1]:
        return bubble_sort(arr, cur_idx + 1, cur_idx + 1, iter + 1)
    else:
        arr[idx], arr[idx - 1] = arr[idx - 1], arr[idx]
        return bubble_sort(arr, idx - 1, cur_idx, iter + 1)
    
    


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    # Get largest number
    largest_num = 0
    sorted_arr = [0] * len(arr)

    # Find the largest Number
    for index in range(0, len(arr) - 1):
        if type(arr[index]) is not int:
            return 'Error, non-integers are not allowed in Count Sort'
        if arr[index] < 0:
            return 'Error, negative numbers not allowed in Count Sort'
        if arr[index] > largest_num:
            largest_num = arr[index]
    
    # Create list of number indexes
    num_list = [0] * (largest_num + 1)

    # Count our numbers
    for num in arr:
        num_list[num] += 1

    # fill out our sorted array
    cur_index = 0
    for num in range(0, len(num_list)):
        while num_list[num] > 0:
            sorted_arr[cur_index] = num
            num_list[num] -= 1
            cur_index += 1

    return sorted_arr

if __name__ == "__main__":
    print(bubble_sort([5,3,2,4,1,7,6,9,8]))
