# Last updated: 8/30/2025, 6:04:37 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = defaultdict(int)

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for key, value in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (value, key))
            else:
                heapq.heappushpop(heap, (value, key))

        return [num for value, num in heap]

