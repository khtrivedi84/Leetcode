class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Clarifying question(s):
        # Is it sorted?
        # Will there be atleast one element in the array?
        # What to do incase of overlap of exact numbers (e.g last element's end time is 4 and next element's start is also 4) ?

        # Sorting
        intervals.sort(key = lambda x: x[0])

        # Output array
        output = [intervals[0]]

        for i in range(1,len(intervals)):
            curr_start = intervals[i][0]
            last_end = output[-1][1]

            if curr_start <= last_end:
                output[-1][1] = max(last_end, intervals[i][1])
            else:
                output.append(intervals[i])
        
        return output