def binarySearchIterative(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left+right) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


def binarySearchRecursive(self, nums, target, left, right):
    if left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            binarySearchRecursive(nums, target, mid+1, right)

        else:
            binarySearchRecursive(nums, target, left, mid-1)
    return -1
