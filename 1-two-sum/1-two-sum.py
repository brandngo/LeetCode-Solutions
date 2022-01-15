class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      numbers = {}       
        
      for i in range(len(nums)):
        if target - nums[i] in numbers and i != numbers[target - nums[i]]: 
          return [numbers[target - nums[i]], i]
        numbers[nums[i]] = i
            
      return [0, 1]