class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = []
        n = len(position)

        for i in range(0, n):
            cars.append((position[i], speed[i]))
        
        cars.sort(key=lambda x: x[0], reverse=True)

        for car in cars:
            #print (stack)
            time = (target - car[0]) / car[1]
            if len(stack) == 0:
                stack.append(time)
            else:
                if stack[-1] >= time:
                    continue
                else:
                    stack.append(time)

        return len(stack)