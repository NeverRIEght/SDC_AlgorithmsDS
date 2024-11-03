class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_table = {}
        startIndex = 0
        max_length = 0

        # store nums and their last occurrence index as num -> index

        for endIndex in range(len(s)):
            char = s[endIndex]
            if char in hash_table:
                startIndex = max(startIndex, hash_table[char] + 1)
            hash_table[char] = endIndex
            max_length = max(max_length, endIndex - startIndex + 1)

        return max_length
