class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
       #[1,2,2,3,3,3]
       # value: 1 -> frequency: 1
       # 2 -> 2
       # 3 -> 3

       # 3 -> [3]
       # 2 -> 2
       # 1 -> 1

        #2 -> [7]

        top = k
        result = []
        freq_to_nums = {} # key: frequency -> value: List of nums @ that freq
        num_to_freq = {} # key: num -> value: freq

        for num in nums:
            if num not in num_to_freq:
                num_to_freq[num] = 1
            else: 
                num_to_freq[num] += 1
        
        #print(num_to_freq)

        for num in num_to_freq:
            freq = num_to_freq[num]
            if freq not in freq_to_nums:
                freq_to_nums[freq] = list()
                freq_to_nums[freq].append(num)
            else:
                freq_to_nums[freq].append(num)
        
        #print(freq_to_nums)

        sorted_freqs = sorted(freq_to_nums.items(), key=lambda x: x[0], reverse=True)

        #print(freq_to_nums)

        amount_of_frequencies = len(freq_to_nums)

        for freq, elem_list in sorted_freqs:
            for elem in elem_list:
                if top > 0:
                    result.append(elem)
                    top -= 1           

        return result
                

            




                

