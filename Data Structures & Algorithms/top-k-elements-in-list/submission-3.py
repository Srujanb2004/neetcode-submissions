class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = Counter(nums).most_common(k)
        op=[]
        for index,value in res:
            op.append(index)
        return op