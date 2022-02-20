class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd=1
        minProd=1
        prodSoFar=max(nums)
        
        for i in nums:
          if (i == 0):
            maxProd = minProd = 1
            continue
          
          tmp = maxProd * i
          maxProd = max(maxProd * i, minProd * i, i)
          minProd = min(tmp, minProd * i, i)
          prodSoFar = max(prodSoFar, maxProd)
        return prodSoFar
          