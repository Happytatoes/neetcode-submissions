class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # we need a hash table where the key is the
        # frequency and the value is a list of things in that frequency
        
        val_to_freq = {}

        for num in nums:
            if num in val_to_freq: 
                val_to_freq[num] += 1
            else:
                val_to_freq[num] = 1
                
        buckets = []
        for i in range(0, len(nums) + 1):
            buckets.append([])

        for val in val_to_freq:
            freq = val_to_freq[val]
            buckets[freq].append(val)
    
        result = []
        q = k 
        for idx in range(0, len(nums) + 1):
            real_idx = (len(nums) - idx)
            if len(buckets[real_idx]) != 0:
                for idx_2 in range(0, len(buckets[real_idx])):
                    if q > 0:
                        result.append(buckets[real_idx][idx_2])
                        q -= 1
        
        return result
        