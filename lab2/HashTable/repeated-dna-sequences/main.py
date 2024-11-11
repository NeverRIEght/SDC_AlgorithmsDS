class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []

        hash_table = {}

        for i in range(len(s) - 9):
            sub_str = s[i:i + 10]
            if sub_str in hash_table:
                hash_table[sub_str] += 1
            else:
                hash_table[sub_str] = 1

        duplicates = []
        for key, value in hash_table.items():
            if value > 1:
                duplicates.append(key)

        return duplicates
