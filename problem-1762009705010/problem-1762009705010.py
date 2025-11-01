# Last updated: 11/1/2025, 7:08:25 PM
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        palindrome_s = re.sub(r'[^A-Za-z0-9]', '', s).lower()

        if palindrome_s == '':
            return True

        i = 0
        j = len(palindrome_s) - 1

        while i < j:
            if palindrome_s[i] == palindrome_s[j]:
                i += 1
                j -= 1
            else:
                return False

        return True

        

        