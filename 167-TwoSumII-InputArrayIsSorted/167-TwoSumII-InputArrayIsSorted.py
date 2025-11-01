# Last updated: 11/1/2025, 6:40:30 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            total = numbers[i] + numbers[j]
            if total == target:
                return [i + 1, j + 1]
            elif total > target:
                j -= 1
            else:
                i += 1

                