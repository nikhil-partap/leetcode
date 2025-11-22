class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        out = 0
        for no in nums:
            if no %3 != 0:
                out += 1
        return out 