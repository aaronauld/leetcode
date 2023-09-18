def containsDuplicate(nums):
    seen = {}
    for num in nums:
        if num in seen:
            return True
        seen[num] = 1
    return False


array = [1, 2, 3, 1]

print(containsDuplicate(array))
