class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        count = 0
        p1 = -1  # The second largest number chosen
        p2 = -1  # The largest number chosen
        
        for s, e in intervals:
            # Case 1: No overlap at all
            if s > p2:
                count += 2
                p1 = e - 1
                p2 = e
            
            # Case 2: One number overlaps (p2 is inside, p1 is outside)
            elif s > p1:
                count += 1
                p1 = p2  # The old max becomes the 2nd max
                p2 = e   # The new max is the current end
            
            # Case 3: Both p1 and p2 are inside [s, e]. Do nothing.
            
        return count