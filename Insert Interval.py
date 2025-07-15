class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Clarifying questions:
        # Is input sorted?
        # Are same numbers considered to be overlapping?
        # How to handle empty array edge cases?

        result = []
        n = len(intervals)
        i = 0

        # Insert all intervals that has smaller end time than the new interval's end time
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # Merge all overlapping intervals (if any)
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1 
        
        # After merging, insert the single new interval into the result
        result.append(newInterval)

        # Insert remaining intervals whose start time is greater than the end time of the merged interval
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result