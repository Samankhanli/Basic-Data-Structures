def merge_sorted_arrays(nums1, nums2):
    m, n = len(nums1), len(nums2)
    nums1.extend([0] * n)  
    p1, p2, p = m - 1, n - 1, m + n - 1  

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    
    nums1[:p2 + 1] = nums2[:p2 + 1]


nums1 = [1, 2, 3]
nums2 = [2, 5, 6]
merge_sorted_arrays(nums1, nums2)
print("Merged array:", nums1)