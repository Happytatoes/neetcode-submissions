class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # consider 0 or 1
        if len(s) == 0 or len(s) == 1:
            return len(s)

        res = 0

        l = 0
        r = 1
        sub = set()
        sub.add(s[0])

        while r < len(s):
            
            #print("start")
            #print(sub)

            if s[r] not in sub:
                sub.add(s[r])
                r += 1
            else:
                char = s[r] # r because it's what we just found so we need to remove it
                curr = l
                found = False
                if s[l] == char:
                    found = True
                while not found:
                    # remove from set
                    sub.remove(s[l])
                    l += 1
                    if s[l] == char:
                        found = True
                sub.remove(s[l])
                l += 1
            
            res = max(res, len(sub))
            #print("end")
            #print(sub)
        
        return res











