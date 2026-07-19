class Solution:
    def isPalindrome(self, s: str) -> bool:

        n = len(s)

        first_index = 0
        last_index = n - 1
        
        while first_index < last_index:
            first_char = s[first_index]
            last_char = s[last_index]
            if not first_char.isalnum():
                first_index += 1
                continue
            if not last_char.isalnum():
                last_index -= 1
                continue
            # if we make it here, they are both alnum
            if first_char.lower() != last_char.lower():
                return False
            first_index += 1
            last_index -= 1
                
        return True
            