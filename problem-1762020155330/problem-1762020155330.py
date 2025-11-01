# Last updated: 11/1/2025, 10:02:35 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_area = 0

        while i < j:
            width = j - i
            h = min(height[i], height[j])
            area = width * h
            max_area = max(max_area, area)

            if height[j] < height[i]:
                j -= 1
            else:
                i += 1

        return max_area
