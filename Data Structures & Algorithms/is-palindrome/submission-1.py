import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s_cleaned = re.sub(r"[^a-z0-9]","",s)
        if s_cleaned == s_cleaned[::-1]:
            return True
        return False
