import exam2

nums1 = [1, -1, 0, 2]
assert exam2.q2_get_last_index(nums1, 1) == 0
assert exam2.q2_get_last_index(nums1, -1) == 1
assert exam2.q2_get_last_index(nums1, 4) == -1

nums2 = [1, -1, 0, 1]
assert exam2.q2_get_last_index(nums2, 1) == 3
assert exam2.q2_get_last_index(nums2, 0) == 2

nums2 = [1, 1, 1, 1]
assert exam2.q2_get_last_index(nums2, 1) == 3
assert exam2.q2_get_last_index(nums2, 0) == -1