class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned=""
        for char in s:
            ##if char ==" ":
              ##  continue      ##NOT NEEDED BCZ ALPHANUM ONLY ALLOWS DIGUITS AND NUMBERS , IGNORES THE SPACES
            if char.isalnum():
                cleaned+=char.lower()
        return cleaned == cleaned[::-1]