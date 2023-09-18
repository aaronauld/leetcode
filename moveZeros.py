def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    anchor = 0
    for explorer in range(len(nums)):
        if nums[explorer] != 0:
            nums[anchor], nums[explorer] = nums[explorer], nums[anchor]
            anchor += 1
    return nums


array = [0, 1, 0, 3, 5, 13]
print(moveZeroes(array))
