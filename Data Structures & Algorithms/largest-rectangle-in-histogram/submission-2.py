class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
       
        max_area = 0
        stack = [] # height, start index for evaluation

        for i in range(len(heights)):
            start = i 
            while stack and stack[-1][0] > heights[i]:
                hei, idx = stack.pop()
                max_area = max(max_area, hei * (i - idx))
                start = idx
            stack.append((heights[i], start))

        while stack:
            hei, idx = stack.pop()
            max_area = max(max_area, hei * (len(heights) - idx))

        return max_area

