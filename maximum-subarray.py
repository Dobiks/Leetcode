class Solution:
    def maxSubArray(self, nums) -> int:
        biggest = -9999999
        for a in range(len(nums)):
            for b in range(len(nums),0,-1):
                val = sum(nums[a:b])
                if val > biggest and len(nums[a:b])!=0:
                    biggest = val
        return biggest
