list = [1, 2, 3, 4, 5, 6]

def create_staircase1(nums):
  while len(nums) != 0:
    step = 1
    subsets = []
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False

  return subsets

def create_staircase2(nums):
  step = 1
  subsets = []
  while len(nums) != 0:
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False
      
  return subsets


print(create_staircase1(list))
print("_____________________________________")
print(create_staircase2(list))