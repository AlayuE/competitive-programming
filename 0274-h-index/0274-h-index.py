class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h = 0
        j = 0
        for i in range(len(citations)-1,-1,-1):
            if citations[i] > j:
                h += 1
            j += 1
        return h
        