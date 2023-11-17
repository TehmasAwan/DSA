def multiway_merge_sort(arr):
    if len(arr) <= 1:
        return arr

   
    sublist_size = len(arr) // 3

    
    sublist1 = arr[:sublist_size]
    sublist2 = arr[sublist_size:2*sublist_size]
    sublist3 = arr[2*sublist_size:]

    
    sublist1 = multiway_merge_sort(sublist1)
    sublist2 = multiway_merge_sort(sublist2)
    sublist3 = multiway_merge_sort(sublist3)

    
    return merge_three(sublist1, sublist2, sublist3)

def merge_three(sublist1, sublist2, sublist3):
    merged = []
    i = j = k = 0

    while i < len(sublist1) and j < len(sublist2) and k < len(sublist3):
        min_val = min(sublist1[i], sublist2[j], sublist3[k])
        merged.append(min_val)
        if sublist1[i] == min_val:
            i += 1
        elif sublist2[j] == min_val:
            j += 1
        else:
            k += 1

    
    merged.extend(sublist1[i:])
    merged.extend(sublist2[j:])
    merged.extend(sublist3[k:])

    return merged

# Example usage:
arr = [5, 2, 9, 3, 6, 1, 8, 4, 7]
sorted_arr = multiway_merge_sort(arr)
print("Sorted using Three-Way Merge Sort:", sorted_arr)
