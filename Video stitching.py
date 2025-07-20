class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        if len(clips) == 0:
            return -1

        clips.sort(key = lambda x: x[0])

        if clips[0][0] != 0:
            return -1
        
        i = 0
        ans = 0
        curr_end = 0
        n = len(clips)

        while curr_end < time:
            farthest = curr_end

            while i < n and clips[i][0] <= curr_end:
                farthest = max(farthest, clips[i][1])
                i += 1 
            
            if farthest == curr_end:
                return -1
            
            ans += 1
            curr_end = farthest
        
        return ans