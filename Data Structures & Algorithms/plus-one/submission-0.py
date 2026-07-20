class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        copy = digits
        n = len(copy)
        
        copy[n - 1] += 1

        for i in range(n - 2, -1, -1):
            if copy[i + 1] == 10:
                copy[i + 1] = 0
                copy[i] += 1
        
        if copy[0] == 10:
            copy = [1, 0] + copy[1:]

        return copy