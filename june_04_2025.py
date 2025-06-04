# 3403. Find the Lexicographically Largest String From the Box I

'''QUESTION'''
# You are given a string word, and an integer numFriends.

# Alice is organizing a game for her numFriends friends. There are multiple rounds in the game, where in each round:

# word is split into numFriends non-empty strings, such that no previous round has had the exact same split.
# All the split words are put into a box.
# Find the lexicographically largest string from the box after all the rounds are finished.

'''Example-1'''
# Input: word = "dbca", numFriends = 2
# Output: "dbc"
# Explanation: 
# All possible splits are:
# "d" and "bca".
# "db" and "ca".
# "dbc" and "a".

'''Example-2'''
# Input: word = "gggg", numFriends = 4
# Output: "g"
# Explanation: 
# The only possible split is: "g", "g", "g", and "g".

'''Constraints:'''
# 1 <= word.length <= 5 * 103
# word consists only of lowercase English letters.
# 1 <= numFriends <= word.length

'''SOLUTION'''
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        max_substrng = ''
        substrng_size = len(word) - numFriends + 1

        for i in range(len(word)):
            max_substrng = max(max_substrng, word[i:i + substrng_size])

        return max_substrng

'''💡💡💡💡💡'''
# Topics Used: String Manipulation, Sliding Window
# Time Complexity: O(n), 
# Space Complexity: O(1),
