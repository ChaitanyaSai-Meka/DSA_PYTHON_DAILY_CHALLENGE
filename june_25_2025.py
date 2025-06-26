# 2040. Kth Smallest Product of Two Sorted Arrays

'''QUESTION'''
# Given two sorted 0-indexed integer arrays nums1 and nums2 as well as an integer k, return the kth (1-based) smallest product of nums1[i] * nums2[j] where 0 <= i < nums1.length and 0 <= j < nums2.length.

'''Example-1'''
# Input: nums1 = [2,5], nums2 = [3,4], k = 2
# Output: 8
# Explanation: The 2 smallest products are:
# - nums1[0] * nums2[0] = 2 * 3 = 6
# - nums1[0] * nums2[1] = 2 * 4 = 8
# The 2nd smallest product is 8.

'''Example-2'''
# Input: nums1 = [-4,-2,0,3], nums2 = [2,4], k = 6
# Output: 0
# Explanation: The 6 smallest products are:
# - nums1[0] * nums2[1] = (-4) * 4 = -16
# - nums1[0] * nums2[0] = (-4) * 2 = -8
# - nums1[1] * nums2[1] = (-2) * 4 = -8
# - nums1[1] * nums2[0] = (-2) * 2 = -4
# - nums1[2] * nums2[0] = 0 * 2 = 0
# - nums1[2] * nums2[1] = 0 * 4 = 0
# The 6th smallest product is 0.

'''Example-3'''
# Input: nums1 = [-2,-1,0,1,2], nums2 = [-3,-1,2,4,5], k = 3
# Output: -6
# Explanation: The 3 smallest products are:
# - nums1[0] * nums2[4] = (-2) * 5 = -10
# - nums1[0] * nums2[3] = (-2) * 4 = -8
# - nums1[4] * nums2[0] = 2 * (-3) = -6
# The 3rd smallest product is -6.

'''Constraints:'''
# 1 <= nums1.length, nums2.length <= 5 * 104
# -105 <= nums1[i], nums2[j] <= 105
# 1 <= k <= nums1.length * nums2.length
# nums1 and nums2 are sorted.

'''SOLUTION'''
class Solution:
  def kthSmallestProduct(
      self,
      nums1: list[int],
      nums2: list[int],
      k: int,
  ) -> int:
    A1 = [-num for num in nums1 if num < 0][::-1]
    A2 = [num for num in nums1 if num >= 0]
    B1 = [-num for num in nums2 if num < 0][::-1]
    B2 = [num for num in nums2 if num >= 0]

    negCount = len(A1) * len(B2) + len(A2) * len(B1)

    if k > negCount: 
      k -= negCount
      sign = 1
    else:
      k = negCount - k + 1  
      sign = -1
      B1, B2 = B2, B1

    def numProductNoGreaterThan(A: list[int], B: list[int], m: int) -> int:
      ans = 0
      j = len(B) - 1
      for i in range(len(A)):
        while j >= 0 and A[i] * B[j] > m:
          j -= 1
        ans += j + 1
      return ans

    l = 0
    r = 10**10

    while l < r:
      m = (l + r) // 2
      if (numProductNoGreaterThan(A1, B1, m) +
              numProductNoGreaterThan(A2, B2, m) >= k):
        r = m
      else:
        l = m + 1

    return sign * l

'''💡💡💡💡💡'''
# Topics Used: Binary Search, Two Pointers, Prefix Arrays (conceptually for counting)
# Time Complexity: O((n + m) * log(MAX))
# Space Complexity: O(n + m)
