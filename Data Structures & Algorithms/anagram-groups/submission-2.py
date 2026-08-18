class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freq_to_list = {} # key: frequencies of the letters, value: list of strings that have those letters at those frequencies

        for string in strs:
            freq = [0] * 26
            for char in string:
                char_value = ord(char) - ord('a')
                freq[char_value] += 1
            
            freq_tuple = tuple(freq)

            if freq_tuple in freq_to_list:
                freq_to_list[freq_tuple].append(string)
            else:
                freq_to_list[freq_tuple] = [string]
        
        result = []
        for list_of_words in freq_to_list.values():
            result.append(list_of_words)
        return result




        