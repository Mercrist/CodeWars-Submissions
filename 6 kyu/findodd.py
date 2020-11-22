def find_it(seq):
    times = 0
    for nums in seq:
        for nums2 in seq:
            if nums2 == nums:
                times += 1
        if times%2 != 0:
            return nums
        times = 0
