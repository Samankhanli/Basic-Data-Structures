def find_missing_number(nums):
    n = len(nums)
    total = n * (n + 1) // 2
    actual_sum = sum(nums)
    return total - actual_sum


input_nums = [5, 2, 0, 3, 1]
missing_number = find_missing_number(input_nums)
print("Missing number:", missing_number)