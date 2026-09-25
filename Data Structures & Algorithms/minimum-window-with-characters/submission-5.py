class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s):
            return ""
        
        res = (-1, -1)
        res_len = float('inf')
        s_map, t_map = {}, {}
        
        for char in t:
            if char in t_map:
                t_map[char] += 1
            else:
                t_map[char] = 1
                s_map[char] = 0
        
        have, need = 0, len(t_map)
        
        l = 0
        for r in range(0, len(s)):
            
            # we don't have what we need
            if s[r] in s_map:
                s_map[s[r]] += 1
                if s_map[s[r]] == t_map[s[r]]:
                    have += 1
            
            # we do 
            while have == need:
                # update the result
                if (r - l + 1) < res_len:
                    res_len = (r - l + 1)
                    res = (l, r)
                
                # move left pointer forward
                if (s[l]) in s_map:
                    s_map[s[l]] -= 1
                    if s_map[s[l]] < t_map[s[l]]:
                        have -= 1
                l += 1


        if res_len == float('inf'):
            return ""
        else:
            return s[res[0]:res[1]+1]

                





            





