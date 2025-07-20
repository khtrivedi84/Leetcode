class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Solution without putting the longer interval before the shorter one in case of a tie for the start time
        intervals.sort(key = lambda x:x[0])

        prev_start = intervals[0][0]
        prev_end = intervals[0][1]

        count = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] > prev_end:
                count += 1
            else:
                if intervals[i][1] <= prev_end:
                    continue

                # Tie case handled here
                elif prev_start >= intervals[i][0] and prev_end < intervals[i][1]:
                    prev_start = intervals[i][0]
                    prev_end = intervals[i][1]

                else:
                    prev_start = intervals[i][0]
                    prev_end = intervals[i][1]
                    count += 1
        return count + 1
    
        # Solution with tie case handled during sorting

        intervals.sort(key = lambda x: (x[0], -x[1]))
        count = 0
        prev_end = 0
        for i in range(len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if end > prev_end:
                count += 1
                prev_end = end
        return count 