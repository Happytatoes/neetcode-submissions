class Solution:

    def encode(self, strs: List[str]) -> str:
        # array of strs -> single hash str
        newstr = []

        for string in strs:
            newstr.append(str(len(string)))
            newstr.append('#')
            #newstr.append(string)
            for char in string:
                newstr.append(char)

        return ''.join(newstr)    
        
    def decode(self, s: str) -> List[str]:
        # single hash str -> array of strs
        
        answer = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            j += 1
            answer.append(s[j:j+length])
            i = j + length
                
        return answer







