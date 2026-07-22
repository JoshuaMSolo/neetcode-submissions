class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums :
            count[num] += 1
        minHeap = []
        for key, values in count.items() :
            minHeap.append((-values, key))
        heapq.heapify(minHeap)
        res = []
        for _ in range(k) :
            res.append(heapq.heappop(minHeap)[1])
        return res
        