class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        heights.append(0)
        max_area = 0
        n = len(heights)
        stack = []
        
        # index, height
        stack.append( (0, heights[0]) )

        for i in range(1, n):

            #print(stack)

            # while the current height is less than the current top of the stack
            while len(stack) > 0 and heights[i] < stack[-1][1]:
                # pop the top of the stack, calc that area
                my_tuple = stack.pop()
                index = my_tuple[0]
                height = my_tuple[1]

                if len(stack) == 0: 
                    left_boundary = -1 
                else:  
                    left_boundary = stack[-1][0]

                right_boundary = i

                area = ( right_boundary - left_boundary - 1 ) * height
                max_area = max(max_area, area)

            # then add our own index to the stack
            stack.append( (i, heights[i]) )

        return max_area