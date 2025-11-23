class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        
        if total % 3 == 0:
            return total
        
        lis1 = sorted([n for n in nums if n % 3 == 1])
        lis2 = sorted([n for n in nums if n % 3 == 2])

        min_loss = float('inf')

        
        if total % 3 == 1:
            if len(lis1) >= 1:
                min_loss = min(min_loss, lis1[0])
            if len(lis2) >= 2:
                min_loss = min(min_loss, lis2[0] + lis2[1])
        
        elif total % 3 == 2:
            if len(lis2) >= 1:
                min_loss = min(min_loss, lis2[0])
            if len(lis1) >= 2:
                min_loss = min(min_loss, lis1[0] + lis1[1])

        return total - min_loss