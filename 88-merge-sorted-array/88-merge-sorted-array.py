class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # since both are sorted we will go through nums1 and get i number from nums2 compare and swap with g + 1 index of nums1. Then repeat. (this is O(m+n))

        cpy = []
        i2 = 0
        i1 = 0
        for i in range(m+n):
          if (i2 < n and i1 < m and nums1[i1] <= nums2[i2]) or i2 >= n:
            cpy.append(nums1[i1])
            i1+=1
          elif i2 < n:
            cpy.append(nums2[i2])
            i2+=1
            
        print(cpy)
        for i in range(m+n):
          print(i)
          nums1[i]=cpy[i]