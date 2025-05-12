"""
LeetCode 557 Reverse Words in String III
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "Mr Ding"
Output: "rM gniD"
 

Constraints:
1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.

"""



class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''
        l, r = 0, 0 
        while r < len(s):
            if s[r] != ' ':
                r +=1
            else: 
                res += s[l:r+1][::-1]
                r += 1
                l = r
        res += ' '
        res += s[l:r + 2][::-1]
        return res[1:]