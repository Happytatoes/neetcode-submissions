class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        s1_freq = [0] * 26
        s2_freq = [0] * 26
        
        # init s1
        for i in range(0, len(s1)):
            s1_freq[ord(s1[i]) - ord('a')] += 1
        
        # init s2
        for i in range(0, len(s1)):
            s2_freq[ord(s2[i]) - ord('a')] += 1
        
        if s1_freq == s2_freq:
            return True

        l = 0 
        for r in range(len(s1), len(s2)):
            s2_freq[ord(s2[r]) - ord('a')] += 1   
            s2_freq[ord(s2[l]) - ord('a')] -= 1  
            l += 1
            if s1_freq == s2_freq:
                return True

        return False







            




