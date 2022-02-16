class Solution:
    def removeDuplicates(self, nums) -> int:
        nums = list(set(nums))
        nums.sort()
        return len(nums)