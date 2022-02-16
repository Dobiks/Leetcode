class Solution:
    def removeDuplicates(self, nums) -> int:
        nums = list(set(nums))
        nums.sort()
        print(nums)
        return len(nums)

sol = Solution
print(sol.removeDuplicates(sol,[1,1,2]))