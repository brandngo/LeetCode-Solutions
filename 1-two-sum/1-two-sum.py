class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      numbers = {}
      
      for i in range(len(nums)):
        numbers[nums[i]] = i
        
      for i in range(len(nums)):
        if numbers.get(target - nums[i]) and i != numbers[target - nums[i]]: 
          return [numbers[target - nums[i]], i]
            
      return [0, 1]