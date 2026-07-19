class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        valid_triples = []

        nums.sort()
        n = len(nums)

        for i in range(0, n - 1):

            first_index = 0
            last_index = n - 1

            while first_index < last_index: 
                if first_index == i:
                    first_index += 1
                    continue
                if last_index == i:
                    last_index -= 1
                    continue
                curr_sum = nums[i] + nums[first_index] + nums[last_index]

                if curr_sum == 0:
                    triplet = [nums[i], nums[first_index], nums[last_index]]   
                    triplet.sort()
                    if triplet not in valid_triples:
                        valid_triples.append(triplet) 
                    first_index += 1
                    continue

                elif curr_sum > 0: 
                    last_index -= 1
                    continue

                else:
                    first_index += 1
                    continue

        return list(valid_triples)






