class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        n = len(numbers)

        first_index = 0
        last_index = n - 1

        while True:
            currSum = numbers[first_index] + numbers[last_index]
            if currSum == target:
                return [first_index + 1, last_index + 1]
            elif currSum > target:
                last_index -= 1
                continue
            else:
                first_index += 1
                continue




