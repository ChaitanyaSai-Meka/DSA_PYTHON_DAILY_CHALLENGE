# 2099. Find Subsequence of Length K With the Largest Sum

'''QUESTION'''
# You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.
# Return any such subsequence as an integer array of length k.
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

'''Example-1'''
# Input: nums = [2,1,3,3], k = 2
# Output: [3,3]
# Explanation:
# The subsequence has the largest sum of 3 + 3 = 6.

'''Example-2'''
# Input: nums = [-1,-2,3,4], k = 3
# Output: [-1,3,4]
# Explanation: 
# The subsequence has the largest sum of -1 + 3 + 4 = 6.

'''Example-3'''
# Input: nums = [3,4,3,3], k = 2
# Output: [3,4]
# Explanation:
# The subsequence has the largest sum of 3 + 4 = 7. 
# Another possible subsequence is [4, 3].

'''Constraints:'''
# 1 <= nums.length <= 1000
# -105 <= nums[i] <= 105
# 1 <= k <= nums.length

'''SOLUTION'''
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        idx_nums = [(num, idx) for idx, num in enumerate(nums)]
        idx_nums.sort(key=lambda x: -x[0])
        top_k = idx_nums[:k]
        top_k.sort(key=lambda x: x[1])
        return [val for val, idx in top_k]

'''💡💡💡💡💡'''
# Topics Used: Greedy, Sorting, Index Tracking
# Time Complexity: O(n log n)
# Space Complexity: O(n)
