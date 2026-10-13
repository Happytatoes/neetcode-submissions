class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        n = len(position)
        stack = []
        pairs = [0] * n # pos, target
        crashes = 0
        
        for i in range(n):
            pairs[i] = (position[i], speed[i])

        pairs.sort(key = lambda x : x[0])
        
        for i in range(n):
            destiny = (target - pairs[i][0]) / pairs[i][1]
            while stack and destiny >= stack[-1]:
                stack.pop()
                crashes += 1
            stack.append(destiny)
        
        return n - crashes