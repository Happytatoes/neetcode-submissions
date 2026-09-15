class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()

        def dfs(curr_sum, curr_list, index):
            if curr_sum == target:
                res.append(curr_list.copy())
                return
            if index >= len(candidates) or curr_sum > target:
                return
            
            # choice 1: include the element
            curr_list.append(candidates[index])
            dfs(curr_sum + candidates[index], curr_list, index + 1)

            # choice 2: do not include the element
            curr_list.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            dfs(curr_sum, curr_list, index + 1)

        dfs(0, [], 0)

        return res









