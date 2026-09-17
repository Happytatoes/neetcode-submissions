class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def dfs(have, could_add):
            if len(have) == len(nums):
                res.append(have.copy())
                return
            
            for elem in could_add.copy():
                have.append(elem)
                could_add.remove(elem)
                dfs(have, could_add)
                have.pop()
                could_add.append(elem)

        dfs([], nums.copy())

        return res