from random import randrange

from scipy import rand


class Solution:
    def maxSubArray(self, nums) -> int:
        biggest = -9999999
        for a in range(len(nums)):
            for b in range(len(nums),0,-1):
                val = sum(nums[a:b])
                if val > biggest and len(nums[a:b])!=0:
                    biggest = val
        return biggest

test = Solution
length = randrange(0,30)
l = []
for a in range(length):
    l.append(randrange(0,30))
print(test.maxSubArray(test,l))