class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[0])
        arrows = 1
        prev_start = points[0][0]
        prev_end = points[0][1]
        for i in range(1, len(points)):
            curr_start = points[i][0]
            curr_end = points[i][1]

            # Overlap
            if prev_start <= curr_end and curr_start <= prev_end:
                prev_start = max(prev_start, curr_start)
                prev_end = min(prev_end, curr_end)
            else:   # No overlap
                arrows += 1
                prev_start = curr_start
                prev_end = curr_end
        return arrows