# 440. K-th Smallest in Lexicographical Order

'''QUESTION'''
# Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

'''Example-1'''
# Input: n = 13, k = 2
# Output: 10
# Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.

'''Example-2'''
# Input: n = 1, k = 1
# Output: 1

'''Constraints:'''
# 1 <= k <= n <= 109

'''SOLUTION'''
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(pre,n):
            count = 0
            curr = pre
            nxt_pre = pre + 1
            while curr <= n:
                count += min(n + 1, nxt_pre) - curr
                curr *= 10
                nxt_pre *= 10
            return count

        curr = 1
        k = k - 1 
        while k > 0:
            steps = count_steps(curr, n)
            if steps <= k:
                k -= steps
                curr += 1
            else:
                k -= 1
                curr *= 10
        return curr

'''💡💡💡💡💡'''
# Topics Used: Trie-like Traversal, Greedy, Depth-First Generation, Number Manipulation
# Time Complexity: O(log(n)^2)
# Space Complexity: O(1)
