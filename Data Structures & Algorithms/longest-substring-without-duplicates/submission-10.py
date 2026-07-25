class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        l = 0
        max_len = 0
        curr = set()

        if n < 2:
            return n

        curr.add(s[0])

        for i in range(1, n):
            r = i
            while s[r] in curr:
                curr.remove(s[l])
                l += 1
            curr.add(s[r])

            if len(curr) > max_len:
                max_len = len(curr)                

        return max_len




