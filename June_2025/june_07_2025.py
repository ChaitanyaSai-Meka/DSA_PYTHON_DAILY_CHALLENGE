# 3170. Lexicographically Minimum String After Removing Stars

'''QUESTION'''
# You are given a string s. It may contain any number of '*' characters. Your task is to remove all '*' characters.

# While there is a '*', do the following operation:

# Delete the leftmost '*' and the smallest non-'*' character to its left. If there are several smallest characters, you can delete any of them.
# Return the lexicographically smallest resulting string after removing all '*' characters.

'''Example-1'''
# Input: s = "aaba*"
# Output: "aab"
# Explanation:
# We should delete one of the 'a' characters with '*'. If we choose s[3], s becomes the lexicographically smallest.

'''Example-2'''
# Input: s = "abc"
# Output: "abc"
# Explanation:
# There is no '*' in the string.

'''Constraints:'''
# 1 <= s.length <= 105
# s consists only of lowercase English letters and '*'.
# The input is generated such that it is possible to delete all '*' characters.

'''SOLUTION'''
class Solution:
  def clearStars(self, s: str) -> str:
    ans = list(s)
    buckets = [[] for _ in range(26)]

    for i, c in enumerate(s):
      if c == '*':
        ans[i] = ''
        for j in range(26):
            if len(buckets[j]) > 0:
                break
        ans[buckets[j].pop()] = ''
      else:
        buckets[ord(c) - ord('a')].append(i)

    return ''.join(ans)

'''💡💡💡💡💡'''
# Topics Used: Array, Stack-like Processing, Greedy, String, Bucketing
# Time Complexity: O(n)
# Space Complexity: O(n)
