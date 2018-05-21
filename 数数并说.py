class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ""
        res = "1"
        while n - 1 > 0:
            n -= 1
            cur = ""
            i = 0
            while i < len(res):
                count = 1
                while (i + 1 < len(res) and res[i] == res [i + 1]):
                    count +=1
                    i += 1
                cur += str(count) + res[i]
                i += 1
            res = cur
        return res
        