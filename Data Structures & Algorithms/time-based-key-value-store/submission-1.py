class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].append((value, timestamp))
        else:
            self.time_map[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        
        # binary search the indices array of tuples at time_map[key] and compare them to the target timestamp
        res = ""
        values = self.time_map[key]
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2
            # candidate timestamp is earlier or equal to target timestamp
            # valid, try later times. latest one ends up as res
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            # candidate timestamp is later than target timestamp
            # invalid, try earlier times.  
            else:
                r = m - 1

        return res
                
        

