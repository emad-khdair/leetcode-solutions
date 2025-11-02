# Last updated: 11/2/2025, 9:08:45 PM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []

        i = 0
        j = len(nums) - 1

        while i <= j:
            left = nums[i] * nums[i]
            right = nums[j] * nums[j]

            if left > right:
                result.append(left)
                i += 1
            else:
                result.append(right)
                j -= 1
        
        return result[::-1]
        