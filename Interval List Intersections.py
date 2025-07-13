class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # Brute force
        output = []
        for a in firstList:
            for b in secondList:
                start = max(a[0], b[0])
                end = min(a[1], b[1])
                if start <= end:  # This confirms there is an overlap
                    output.append([start, end])
        return output
    
        # Check for edge cases
        if not secondList or not firstList:
            return []

        output = []

        p1 = 0
        p2 = 0

        while p1 < len(firstList) and p2 < len(secondList):
            s1 = firstList[p1][0]
            e1 = firstList[p1][1]

            s2 = secondList[p2][0]
            e2 = secondList[p2][1]

            # Check if overlap exist
            if s1 <= e2 and s2 <= e1:
                output.append([max(s1,s2), min(e1,e2)])

            if e1 <= e2:
                p1 += 1
            else:
                p2 += 1
        return output