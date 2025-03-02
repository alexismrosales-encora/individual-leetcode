from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        """
        Solution for Leetcode problem 2744
        Find maximum number of strings pairs

        Reasoning: Create a set of every word if it doesn't exists, if it exists in reverse count 1

        Approach: A set of words is useful because if a word exists in reverse, the counter increases.
        If it does not exist, we add it as a new element in the set.
        If the word is already in the set, we simply ignore it.
        """
        mapWords = set()
        pairs = 0
        for word in words:
            # If there is a new word in the map, verifies if the word in reverse exists in the map
            if word not in mapWords:
                if word[::-1] in mapWords:
                    # Counting coincidences
                    pairs += 1
                else:
                    mapWords.add(word)
        return pairs

