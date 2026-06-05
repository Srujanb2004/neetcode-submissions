class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=Counter(nums).most_common(k)
        op=[]
        for num,index in res:
            op.append(num)
        return op