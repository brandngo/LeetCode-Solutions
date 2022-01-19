class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      count = {}
      
      for i, value in enumerate(nums):
        if (value in count):
          return True
        else:
          count[value] = 1
      
      return False