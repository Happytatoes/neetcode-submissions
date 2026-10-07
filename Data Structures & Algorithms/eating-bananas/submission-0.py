class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def eatingHrs(k):
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i] / k)
            return hours 

        min_k, max_k = 1, max(piles)
        min_valid_k = max_k

        while min_k <= max_k:
            candidate = (min_k + max_k) // 2

            if eatingHrs(candidate) > h:
                # it takes more hours than we have. raise k.
                min_k = candidate + 1
            else: 
                min_valid_k = min(min_valid_k, candidate)
                max_k = candidate - 1
                
        return min_valid_k
        