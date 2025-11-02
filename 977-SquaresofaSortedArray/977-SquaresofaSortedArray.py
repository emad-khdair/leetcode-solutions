# Last updated: 11/2/2025, 8:19:12 PM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            result.append(nums[i] ** 2)

        result.sort()

        return result
            