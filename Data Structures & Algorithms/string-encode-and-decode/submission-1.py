class Solution:

    def encode(self, strs: List[str]) -> str:
        # number, slash, string
        result = ""

        for string in strs:
            result += str(len(string))
            result += "/"
            result += string
        
        return result
        
    def decode(self, s: str) -> List[str]:

        result = []

        i = 0
        while i < len(s):

            # processing each word
            curr_len = ""
            print(i)
            while s[i] != '/':
                curr_len += str(s[i])
                i += 1
            word_len = int(curr_len)
            i += 1 # for the slash
            new_string = s[i:i+word_len]
            result.append(new_string)
            i += word_len

        return result











                




