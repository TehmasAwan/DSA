def merge_sort_descending(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_sorted = merge_sort_descending(left_half)
    right_sorted = merge_sort_descending(right_half)

    return merge_descending(left_sorted, right_sorted)

def merge_descending(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] >= right[j]:  # Compare in reverse order for descending sort
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

# Example usage:
arr = [5, 2, 9, 3, 6, 1]
sorted_arr_desc = merge_sort_descending(arr)
print("Sorted in descending order:", sorted_arr_desc)
