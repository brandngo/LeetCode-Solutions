class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Naive approach: more memory
        """
        for i in range(k):
          shifted=newNums[len(newNums)-1:len(newNums)]
          ori=newNums[:len(newNums)-1]
          newNums=shifted+ori
        
        for i in range(len(nums)):
          nums[i]=newNums[i]
        """
        
        # Reversal appraoch: O(1) memory
        k = k % len(nums)
        
        nums[:] = nums[::-1]
        nums[:] = nums[:k][::-1] + nums[k:][::-1]
        

        
        