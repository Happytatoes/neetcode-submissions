class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        ptr_1 = cost[n - 1]
        ptr_2 = cost[n - 2]

        for i in range(n - 3, -1, -1):
            new = cost[i] + min(ptr_1, ptr_2)
            temp = ptr_2
            ptr_2 = new
            ptr_1 = temp

        return min(ptr_1, ptr_2)