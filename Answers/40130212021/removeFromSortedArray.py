def remove_duplicates(nums):
    if not nums:
        return 0

    index = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[index - 1]:
            nums[index] = nums[i]
            index += 1

    return index


input_nums = [1, 1, 2, 2, 3, 4, 5, 5]
new_length = remove_duplicates(input_nums)
print("New array:", input_nums[:new_length])
print("New length:", new_length)