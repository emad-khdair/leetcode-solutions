# Last updated: 9/15/2025, 8:10:15 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], index]
            num_map[num] = index 