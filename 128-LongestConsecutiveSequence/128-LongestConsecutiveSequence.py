# Last updated: 10/27/2025, 4:42:25 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        longest = 0

        for n in num_set:
            if n - 1 not in num_set:
                current = n
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest