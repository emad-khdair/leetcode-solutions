# Last updated: 9/17/2025, 10:45:33 AM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right = 1, 1

        for i in range(n):
            result[i] = left
            left *= nums[i]

        for i in range(n - 1, -1, -1):
            result[i] *= right
            right *= nums[i]
            
        return result