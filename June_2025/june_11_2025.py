# 3445. Maximum Difference Between Even and Odd Frequency II

'''QUESTION'''
# You are given a string s and an integer k. Your task is to find the maximum difference between the frequency of two characters, freq[a] - freq[b], in a substring subs of s, such that:
# subs has a size of at least k.
# Character a has an odd frequency in subs.
# Character b has an even frequency in subs.
# Return the maximum difference.
# Note that subs can contain more than 2 distinct characters.

'''Example-1'''
# Input: s = "12233", k = 4
# Output: -1
# Explanation:
# For the substring "12233", the frequency of '1' is 1 and the frequency of '3' is 2. The difference is 1 - 2 = -1.

'''Example-2'''
# Input: s = "1122211", k = 3
# Output: 1
# Explanation:
# For the substring "11222", the frequency of '2' is 3 and the frequency of '1' is 2. The difference is 3 - 2 = 1.

'''Example-3'''
# Input: s = "110", k = 3
# Output: -1

'''Constraints:'''
# 3 <= s.length <= 3 * 104
# s consists only of digits '0' to '4'.
# The input is generated that at least one substring has a character with an even frequency and a character with an odd frequency.
# 1 <= k <= s.length

'''SOLUTION'''
class Solution:
  def maxDifference(self, s: str, k: int) -> int:
    ans = -math.inf
    permutations = [(a, b) for a in '01234' for b in '01234' if a != b]

    for a, b in permutations:
      minDiff = collections.defaultdict(lambda: math.inf)
      prefixA = [0]
      prefixB = [0]

      l = 0
      for r, c in enumerate(s):
        prefixA.append(prefixA[-1] + int(c == a))
        prefixB.append(prefixB[-1] + int(c == b))
        while (r - l + 1 >= k and
               prefixA[l] < prefixA[-1] and 
               prefixB[l] < prefixB[-1]):
          paritiesKey = (prefixA[l] % 2, prefixB[l] % 2)
          minDiff[paritiesKey] = min(minDiff[paritiesKey],
                                     prefixA[l] - prefixB[l])
          l += 1
        ans = max(ans, (prefixA[-1] - prefixB[-1]) -
                  minDiff[(1 - prefixA[-1] % 2, prefixB[-1] % 2)])

    return ans

'''💡💡💡💡💡'''
# Topics Used: HashMap (collections.defaultdict), Prefix Sum, Sliding Window, Conditional Logic, Frequency Counting  
# Time Complexity: O(n)  
# Space Complexity: O(1)
