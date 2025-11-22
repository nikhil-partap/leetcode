class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        out = 0

        pt1 = -1
        pt2 = -1

        for start , end in intervals:

            if start > pt2:
                out += 2
                pt1 = end -1
                pt2 = end
            elif start > pt1:
                out += 1
                pt1 = pt2
                pt2 = end
        return out