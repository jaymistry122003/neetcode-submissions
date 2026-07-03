class Solution:
    def isPalindrome(self, s: str) -> bool:
         cleaned_s = "".join(char.lower() for char in s if char.isalnum())
    
    # Compare the cleaned string to its reverse
         return cleaned_s == cleaned_s[::-1]
     
        