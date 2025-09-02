# Last updated: 9/2/2025, 9:33:21 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], index]
            num_map[num] = index

    