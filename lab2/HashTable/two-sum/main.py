class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # store nums and their indices as num -> index

        hash_table = {}
        for index, num in enumerate(nums):
            tn = target - num
            if tn in hash_table:
                return [hash_table[tn], index]
            hash_table[num] = index
        return []