class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_list_1 = list(s)
        my_list_2 = list(t)

        my_list_1.sort()
        my_list_2.sort()
        
        return my_list_1 == my_list_2