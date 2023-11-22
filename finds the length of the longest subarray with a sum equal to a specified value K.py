
def longest_subarray_with_sum(nums, K):
    max_length = 0
    cumulative_sum = 0
    sum_indices = {0: -1}  

    for i, num in enumerate(nums):
        cumulative_sum += num

        difference = cumulative_sum - K

        if difference in sum_indices:
            max_length = max(max_length, i - sum_indices[difference])

        if cumulative_sum not in sum_indices:
            sum_indices[cumulative_sum] = i

    return max_length

arr = [10, 5, 2, 7, 1, 9]
target_sum = 15
result = longest_subarray_with_sum(arr, target_sum)
print(f"Length of the longest subarray with sum {target_sum}: {result}")
