def max_subarray_sum(nums):
    max_sum = float()
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


input_nums = [-2, -1, -3, 4, -1, 2, 1, -5, 4]
max_sum = max_subarray_sum(input_nums)
print( max_sum)