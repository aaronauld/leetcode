def maxSubArray(nums):
    maxSum = float('-inf')
    tempSum = 0
    for number in nums:
        tempSum += number
        maxSum = max(maxSum, tempSum)
        if tempSum < 0:
            tempSum = 0
    return maxSum


array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(maxSubArray(array))
