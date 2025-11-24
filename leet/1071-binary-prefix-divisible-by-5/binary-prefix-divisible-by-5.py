class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        out: List[bool] = []
        b = 0

        for no in nums:
            b = (b * 2 + no) % 5       
            out.append(b == 0)          
        return out