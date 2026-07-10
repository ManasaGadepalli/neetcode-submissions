class Solution:
    def convert_string(self, st:str) -> str:
        pieces = []
        for char in st:
            if char.isalnum():
                pieces.append(char.lower())
        return "".join(pieces)

    def isPalindrome(self, s: str) -> bool:
        new_string = self.convert_string(s) 
        reverse_string = new_string[::-1]
        if new_string == reverse_string:
            return True

        return False
    
    

        