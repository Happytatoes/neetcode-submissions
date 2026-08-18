class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #[1,2,4,6]

        #prefix: [1, 1, 2, 8, 48] 
        #postfix: [48, 48, 24, 6, 1]

        output = [1] * len(nums)

        for i in range(0, len(nums) - 1):
            output[i + 1] = output[i] * nums[i]

        postfix = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            postfix[i - 1] = postfix[i] * nums[i]
        postfix[-1] = 1

        for i in range(0, len(nums)):
            output[i] *= postfix[i]

        return output







