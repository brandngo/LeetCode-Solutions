class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]
        m = 1
        for i in range(1, len(nums)+1):
          answer.append(answer[i-1] * nums[i-1])
        
        del answer[len(answer)-1]
        for i in range(len(answer)-1, -1, -1):
          answer[i] *= m
          m *= nums[i]
        
        return answer