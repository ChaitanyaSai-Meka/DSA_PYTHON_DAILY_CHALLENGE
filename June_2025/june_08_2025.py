# 386. Lexicographical Numbers

'''QUESTION'''
# Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.
# You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

'''Example-1'''
# Input: n = 13
# Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]

'''Example-2'''
# Input: n = 2
# Output: [1,2]

'''Constraints:'''
# 1 <= n <= 5 * 104

'''SOLUTION'''
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        curr = 1
        for i in range(n):
            result.append(curr)
            if curr * 10 <= n:
                curr *= 10
            else:
                if curr >= n:
                    curr //= 10
                while curr % 10 == 9 or curr + 1 > n:
                    curr //= 10
                curr += 1
        return result

'''💡💡💡💡💡'''
# Topics Used: Trie-like Traversal, Greedy, Depth-First Generation, Number Manipulation
# Time Complexity: O(n) 
# Space Complexity: O(1)
