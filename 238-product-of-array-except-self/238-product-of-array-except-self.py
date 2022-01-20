class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      mult = [1]
      
      for i in range(1, len(nums)):
        mult.append(mult[i-1] * nums[i-1])
      
      postfix=1
      for i in range(len(nums)-1, -1, -1):
        mult[i] *= postfix
        postfix *= nums[i]
        
      return mult
