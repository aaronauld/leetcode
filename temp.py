file = open(r"C:\Users\aaron\OneDrive\Desktop\Projects\leetcode\input.txt", "r")
maxSum = 0
tempSum = 0
calories = []
for line in file:
    if line == "\n":
        if tempSum > maxSum:
            maxSum = tempSum
        calories.append(tempSum)
        tempSum = 0
    else:
        number = int(float(line.strip("\n")))
        tempSum += number

count = 0
maxSum = 0
for elf in sorted(calories, reverse=True):
    count += 1
    maxSum += elf
    if count == 3:
        break
print(maxSum)
