def get_max(nums):
  if len(nums) == 2:
    return max(nums)
  else:
    return max([get_max(nums[0:-1]), nums[-1]])
                   
print(get_max([8, 2, 20, 4, 5]))