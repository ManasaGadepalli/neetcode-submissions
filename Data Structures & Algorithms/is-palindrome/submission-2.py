class Solution:
    def convert_string(self, st:str) -> str:
        pieces = []
        for char in st:
            if char.isalnum():
                pieces.append(char.lower())
        return "".join(pieces)

    def isPalindrome(self, s: str) -> bool:
        new_str = self.convert_string(s) 
        # Solution 1 
        # reverse_string = new_string[::-1]
        # if new_string == reverse_string:
        #     return True

        # return False
    
        # Solution 2
        left = 0
        right = len(new_str)-1
    
        # 2nd check    
        while left < right:
            if new_str[left] != new_str[right]:
                return False
            left += 1
            right -= 1
        
        return True
            

        