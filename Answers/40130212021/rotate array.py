def rotate_array(nums, k):
    n = len(nums)
    k %= n  
    nums[:] = nums[-k:] + nums[:-k]


input_nums = [1, 2, 3, 4, 5]
k = 2
rotate_array(input_nums, k)
print( input_nums)