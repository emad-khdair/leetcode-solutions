# Last updated: 9/1/2025, 7:46:50 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        heap = []

        for num, freq in freq.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for (freq, num) in heap]

