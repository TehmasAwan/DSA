
def count_frequency(numbers):
    frequency_dict = {}

    for num in numbers:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1

    return frequency_dict

integer_list = [1, 2, 3, 4, 2, 3, 1, 2, 4, 5, 6, 5]
result = count_frequency(integer_list)
print(result)
