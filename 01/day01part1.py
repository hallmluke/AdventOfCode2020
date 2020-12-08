file = open('input.txt', mode = 'r')
lines = file.readlines()
file.close()
nums = []

for line in lines:
    nums.append(int(line))

nums.sort()

left = 0


for num in nums:
    ptr = left + 1
    right = len(nums) - 1
    while ptr < right:
        if nums[left] + nums[ptr] + nums[right] == 2020:
            print(nums[left] * nums[ptr] * nums[right])
            break
        elif nums[left] + nums[ptr] + nums[right] < 2020:
            ptr += 1
        else:
            right -= 1
    left += 1