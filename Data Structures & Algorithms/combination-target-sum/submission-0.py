class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(index, curr, curr_sum):
            if curr_sum == target:
                res.append(curr.copy())
                return
            if curr_sum > target or index >= len(nums):
                return
            
            # decision to include
            curr.append(nums[index])
            dfs(index, curr, curr_sum + nums[index])

            # decision to exclude
            curr.pop()
            dfs(index + 1, curr, curr_sum)


        dfs(0, [], 0)
        return res

                













