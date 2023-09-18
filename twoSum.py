def twoSum(nums, target):
    seen = {}
    for key, value in enumerate(nums):
        remainder = target - value
        if remainder in seen:
            return [seen[remainder], key]
        else:
            seen[value] = key


nums = [1, 2, 3, 7, 8, 9]
target = 9

print(twoSum(nums, target))
