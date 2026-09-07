class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        curr = []

        def dfs(num):

            if num >= len(nums):
                res.append(curr.copy())
                return

            elem = nums[num]
            
            # decision: add the current element
            curr.append(elem)
            dfs(num + 1)

            # decision: do not add the current element
            curr.pop()
            dfs(num + 1)

        dfs(0)

        return res











