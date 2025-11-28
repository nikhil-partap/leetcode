class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lis = set(nums)

        if len(lis) == len(nums):
            return False
        
        return True