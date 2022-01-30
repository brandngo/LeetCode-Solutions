class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = 0
        msoFar = nums[0]
        for i in range(len(nums)):
          if m < 0:
            m = 0
          
          m += nums[i]
          msoFar = max(msoFar, m)
          
        return msoFar