def maximum_product_of_all_but_one(arr):
    n = len(arr)
    num_negative_entries = 0
    min_negative_entry_idx = max_negative_entry_idx = min_positive_entry_idx = -1
    for i in range(n):
        if arr[i] < 0 :
            num_negative_entries+=1
            if min_negative_entry_idx == -1 or arr[i] < arr[min_negative_entry_idx]:
                min_negative_entry_idx = i
            if max_negative_entry_idx == -1 or arr[i] > arr[max_negative_entry_idx]:
                max_negative_entry_idx = i
        else:
            if min_positive_entry_idx == -1 or arr[i] < arr[min_positive_entry_idx]:
                min_positive_entry_idx = i

    if num_negative_entries%2 : #nexclude one negative entry the largest one
        excluded_entry_idx = max_negative_entry_idx

    else:
        if num_negative_entries == n : #all of the entries are negative
            excluded_entry_idx = max_negative_entry_idx
        else:
            excluded_entry_idx = min_positive_entry_idx

    result = multiply_without_one_entry(arr, n, excluded_entry_idx)
    return result


def multiply_without_one_entry(nums, n, excluded_idx) :
    result = 1
    for i in range(n):
        if i != excluded_idx :
            result *= nums[i]
    return result if n else 0

if __name__ == "__main__":
    arr = [3,2,-1,4,-1,6]
    print maximum_product_of_all_but_one(arr)

