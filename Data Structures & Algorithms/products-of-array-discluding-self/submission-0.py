class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        prefix = [1] * n
        suffix = [1] * n

        # create prefix
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        print(prefix)
            

        # create suffix
        i = n - 2
        while i >= -1:
            suffix[i] = suffix[i + 1] * nums[i + 1] 
            i -= 1
        suffix[n-1] = 1
        print(suffix)

        answer = [1] * n
        for i in range(0, n):
            answer[i] = prefix[i] * suffix[i]
            
        return answer

        ''' 1 2 4 6

        create: 

        2x4x6 | 1x4x6 | 1x2x6 | 1x2x4

        (1) 1  2  8

        48  24 6 (1)
        '''

