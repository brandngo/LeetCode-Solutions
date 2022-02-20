class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
      """
        firstProd, secProd, thirdProd = 1, 1, 1
        maxProd = max(nums)
        
        for i in range(len(nums)):
          if nums[i] == 0:
            firstProd, secProd, thirdProd = 1
            continue
          if i % 3 == 0:
            i * nums
     
      
      products = set()
      
      for i in range(2, len(nums)):
        products.add(nums[i] * nums[i-1] * nums[i-2])
        
      
      if len(products) == 0:
        return None
      return max(products)
       """
      
      mins = nums[:]
      
      max1 = max(nums)
      nums.remove(max1)
      max2 = max(nums)
      nums.remove(max2)
      max3 = max(nums)
      
      min1 = min(mins)
      mins.remove(min1)
      min2 = min(mins)
      
      return max(max1*max2*max3, min1*min2*max1)