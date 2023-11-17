def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left_half, left_count = merge_sort(arr[:mid])
    right_half, right_count = merge_sort(arr[mid:])
    sorted_arr, merge_count = merge(left_half, right_half)
    
    total_count = left_count + right_count + merge_count
    return sorted_arr, total_count

def merge(left, right):
    merged = []
    count = 0
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            count += len(left) - i
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged, count

def count_inversions(arr):
    _, inversions = merge_sort(arr)
    return inversions


arr = [1, 3, 5, 2, 4, 6]
inversion_count = count_inversions(arr)
print("Number of inversions:", inversion_count)
