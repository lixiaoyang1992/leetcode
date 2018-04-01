class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        str = ''
        count = 0;
        for i in s:
            index = str.find(i)
            if index > -1:
                if (len(str) > count):
                    count = len(str)
                str = str[index + 1: len(str)]
            str += i
        if (len(str) > count):
            count = len(str)
        return count


a = Solution()
print(a.lengthOfLongestSubstring("bpfbhmipx"))
