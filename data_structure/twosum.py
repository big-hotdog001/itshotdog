## Solution of mine
def findSums(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return nums[i], nums[j]
    
n = int(input())
nums = [2, -3, 7, 11, 15, 17]
num1, num2 = findSums(nums, n)
print(num1, num2)

