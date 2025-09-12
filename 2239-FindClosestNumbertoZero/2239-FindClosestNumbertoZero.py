# Last updated: 9/12/2025, 8:34:21 PM
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]

        for num in nums:
            if abs(num) < abs(closest):
                closest = num
            if abs(num) == abs(closest) and num > closest:
                closest = num

        return closest
         