class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        
        prefix = [float("inf")] * k
        prefix[0] = 0
        res = float("-inf")

        total = 0
        for i ,  n in enumerate(nums):
            total += n
            prefix_len = (i + 1) % k
            res = max(res, total - prefix[prefix_len])

            prefix[prefix_len] = min(prefix[prefix_len] , total)
        
        return res 