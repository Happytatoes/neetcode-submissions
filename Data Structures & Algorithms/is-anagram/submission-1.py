class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # cooler solution

        my_dict_1 = {}
        my_dict_2 = {}
        
        for char in s:
            if my_dict_1.get(char) == None:
                my_dict_1[char] = 0
            else:
                my_dict_1[char] = my_dict_1[char] + 1

        for char in t:
            if my_dict_2.get(char) == None:
                my_dict_2[char] = 0
            else:
                 my_dict_2[char] = my_dict_2[char] + 1

        return my_dict_1 == my_dict_2

        # old solution

        #my_list_1 = list(s)
        #my_list_2 = list(t)

        #my_list_1.sort()
        #my_list_2.sort()
        
        #return my_list_1 == my_list_2