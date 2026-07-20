class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        n = len(heights)

        first_index = 0
        last_index = n - 1

        greatest_area = 0

        while first_index < last_index:
            area = (last_index - first_index) * min(heights[first_index], heights[last_index])
            if area > greatest_area:
                greatest_area = area

            if heights[first_index] >= heights[last_index]:
                last_index -= 1
                continue
            else:
                first_index += 1
                continue

        return greatest_area