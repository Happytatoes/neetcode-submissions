class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x : x[0])

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            end_of_current_interval = res[-1][1]
            
            if intervals[i][0] <= end_of_current_interval:
                res[-1][1] = max(end_of_current_interval, intervals[i][1])
            else:
                res.append(intervals[i])
        
        return res