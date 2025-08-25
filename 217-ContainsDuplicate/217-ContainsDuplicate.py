# Last updated: 8/25/2025, 8:52:33 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
