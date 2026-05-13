class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countedNums = Counter(nums)
        return [item[0] for item in countedNums.most_common(k)]
        