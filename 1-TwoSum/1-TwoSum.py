# Last updated: 8/30/2025, 1:10:52 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [hash_map[complement], index]
            hash_map[num] = index