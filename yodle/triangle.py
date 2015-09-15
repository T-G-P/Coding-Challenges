with open('triangle.txt') as f:
    index = 0
    res = 0
    for line in f:
        nums = list(map(int, line.split()))
        num = max(nums[index:index+2])
        index = nums.index(num)
        res += num

print(res)
