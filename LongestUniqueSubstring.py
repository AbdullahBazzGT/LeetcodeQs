"""Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 """
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        
        left = 0
        right = 0
        greatest = 0
        vs = set()
        
        while right < len(s) - 1:
            while s[right] not in vs:
                vs.add(s[right])
                right += 1
                if right == len(s):
                    break

            if (right - left) > greatest:
                greatest = right - left
            
            vs.remove(s[left])
            left += 1

        return greatest