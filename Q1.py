def summ(nums):
    count = 0
    for num in str(nums):
        count += int(num)
    return count
nums = 123
son = summ(nums)
print(son)