class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_seq_length = 0
        num_set = set(nums)
        for elem in num_set:
            if elem - 1 not in num_set:
            # this could be the start of a sequence
                curr = elem 
                curr_seq_length = 1
                while curr + 1 in num_set:
                    curr_seq_length += 1
                    curr += 1
                if curr_seq_length > longest_seq_length:
                    longest_seq_length = curr_seq_length

        return longest_seq_length
                    