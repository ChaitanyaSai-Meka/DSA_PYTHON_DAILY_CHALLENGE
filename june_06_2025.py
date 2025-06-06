# 2434. Using a Robot to Print the Lexicographically Smallest String

'''QUESTION'''
# You are given a string s and a robot that currently holds an empty string t. Apply one of the following operations until s and t are both empty:

# Remove the first character of a string s and give it to the robot. The robot will append this character to the string t.
# Remove the last character of a string t and give it to the robot. The robot will write this character on paper.
# Return the lexicographically smallest string that can be written on the paper.

'''Example-1'''
# Input: s = "zza"
# Output: "azz"
# Explanation: Let p denote the written string.
# Initially p="", s="zza", t="".
# Perform first operation three times p="", s="", t="zza".
# Perform second operation three times p="azz", s="", t="".

'''Example-2'''
# Input: s = "bac"
# Output: "abc"
# Explanation: Let p denote the written string.
# Perform first operation twice p="", s="c", t="ba". 
# Perform second operation twice p="ab", s="c", t="". 
# Perform first operation p="ab", s="", t="c". 
# Perform second operation p="abc", s="", t="".

'''Example-3'''
# Input: s = "bdda"
# Output: "addb"
# Explanation: Let p denote the written string.
# Initially p="", s="bdda", t="".
# Perform first operation four times p="", s="", t="bdda".
# Perform second operation four times p="addb", s="", t="".

'''Constraints:'''
# 1 <= s.length <= 105
# s consists of only English lowercase letters.

'''SOLUTION'''
class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        min_suff = [''] * n
        min_c = 'z'
        
        for i in range(n - 1, -1, -1):
            if s[i] < min_c:
                min_c = s[i]
            min_suff[i] = min_c
        
        t = []
        p = []
        
        for i in range(n):
            t.append(s[i])
            while t and (i == n - 1 or t[-1] <= min_suff[i + 1]):
                p.append(t.pop())
        
        return ''.join(p)

'''💡💡💡💡💡'''
# Topics Used: Stack, Greedy, String, Suffix Minimum Array
# Time Complexity: O(n), where n is the length of the string s
# Space Complexity: O(n), for the stack, result array, and suffix minimum array
