class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        answer = []
        mymap = {} # list[int] -> list[str]

        for curr_str in strs:
            freqarray = [0] * 26
            curr_word = list(curr_str)
            
            for char in curr_word:
                i = ord(char) - 97 # A = 0, Z = 25
                freqarray[i] += 1

            if str(freqarray) in mymap: # we've seen this pattern before 
                mymap[str(freqarray)].append(curr_str) # add the string to the list at the hash of the frequency

            else: # this is new 
                newlist = [] # create a new list
                newlist.append(curr_str) # add the current string to the list
                mymap[str(freqarray)] = newlist # set the key to the freqarray with the value as the list

        for curr_freqarray in mymap:
            answer.append(mymap[curr_freqarray])

        return answer

            