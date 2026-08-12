class Solution:

    def s_contains_t(self, matched: int, required: int):
        return matched == required

    def minWindow(self, s: str, t: str) -> str:
        
        # edge case
        if len(s) < len(t):
            return ""
        
        s_freq = [0] * 123
        t_freq = [0] * 123

        # build hash for t
        for i in range(len(t)):
            t_freq[ord(t[i])] += 1

        # count how many distinct characters t requires
        required = 0
        for i in range(0, 123):
            if t_freq[i] > 0:
                required += 1

        l = 0
        best_l = -1
        best_r = -1
        n = len(s)
        matched = 0

        for r in range(0, n):

            curr = ord(s[r])
            s_freq[curr] += 1

            if t_freq[curr] > 0 and s_freq[curr] == t_freq[curr]:
                matched += 1

            while self.s_contains_t(matched, required):
                if best_l == -1 or (r - l) < (best_r - best_l):
                    best_l = l
                    best_r = r

                left_curr = ord(s[l])
                if t_freq[left_curr] > 0 and s_freq[left_curr] == t_freq[left_curr]:
                    matched -= 1
                s_freq[left_curr] -= 1
                l += 1

        if best_l == -1:
            return ""

        return s[best_l:best_r + 1]





