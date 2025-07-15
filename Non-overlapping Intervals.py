class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort based on end-time
        intervals.sort(key = lambda x: x[1])

        cnt = 0
        last_end_time = intervals[0][1]
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if start < last_end_time:
                cnt += 1
            else:
                last_end_time = end

        return cnt