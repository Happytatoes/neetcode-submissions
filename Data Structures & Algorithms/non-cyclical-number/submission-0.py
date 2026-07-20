class Solution:
    
    def compute(self, n: int):
    
        res = 0
        digits = []

        while n > 0:
            digits.append(n % 10)
            n //= 10

        for digit in digits:
            res += pow(digit, 2)
        
        return res
    
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        
        curr = n

        while True:
            if curr not in seen:
                seen.add(curr)
            else: 
                if curr == 1:
                    return True
                else:
                    return False

            curr = self.compute(curr)
            

