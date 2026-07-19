class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned_string = ""
        
        for char in s:
            if char.isalnum():
                cleaned_string += str(char.lower())
        
        n = len(cleaned_string)

        for i in range(0, n // 2):
            index = i
            anti_index = n - 1 - i
            if cleaned_string[index] != cleaned_string[anti_index]:
                return False

        return True
            