class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nos = nums

        for i in range(len(nos)):
            if original in nos:
                original *= 2
            else:
                break


        return original 