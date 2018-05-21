class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        s = s.lower()
        s = re.sub('[^a-zA-Z0-9]','',s)
        return s == s[::-1]