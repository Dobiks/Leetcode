from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,a in enumerate(nums):
            for j,b in enumerate(nums):
                if a+b==target and j != i:
                    return [i,j]
            