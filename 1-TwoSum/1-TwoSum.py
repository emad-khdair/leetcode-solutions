# Last updated: 8/31/2025, 4:51:26 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in mp:
                return [mp[complement], index]
            mp[num] = index