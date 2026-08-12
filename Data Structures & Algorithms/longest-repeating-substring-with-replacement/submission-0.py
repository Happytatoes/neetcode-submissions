class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # key is character, value is count
        char_freqs = {}

        max_freq = 0
        l = 0
        res = 0

        n = len(s)

        for r in range(0, n):
            
            char_freqs[s[r]] = 1 + char_freqs.get(s[r], 0)
            max_freq = max(max_freq, char_freqs[s[r]])

            while (r - l + 1) - max_freq > k:
                char_freqs[s[l]] -= 1
                l += 1
            
            # max valid window so far
            res = max(res, r - l + 1)

        return res
            