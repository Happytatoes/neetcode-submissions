class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    
        max_freq = 0
        char_map = {}
        res = 0
        l = 0
        
        for r in range(0, len(s)):
            if s[r] not in char_map:
                char_map[s[r]] = 1
            else:
                char_map[s[r]] += 1
            max_freq = max(max_freq, char_map[s[r]])

            while max_freq + k < (r - l + 1):
                # update map and max_freq
                char_map[s[l]] -= 1
                # maybe unneccesary
                new_max_freq = 0
                if char_map[s[l]] < max_freq:
                    for freq in char_map.values():
                        new_max_freq = max(new_max_freq, freq)
                
                max_freq = new_max_freq

                # move left pointer forward
                l += 1 

            res = max(res, r - l + 1)

        return res














            
