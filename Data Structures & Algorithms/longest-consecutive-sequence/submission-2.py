class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       
        result = 0
        num_set = set(nums)

        for num in num_set:
            if not num - 1 in num_set:
                # this is the start of a consecutive sequence
                i = num + 1
                seq_length = 1
                while i in num_set:
                    seq_length += 1
                    i += 1
                result = max(result, seq_length)

        return result
