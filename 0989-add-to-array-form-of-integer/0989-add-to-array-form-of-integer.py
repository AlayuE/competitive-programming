class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        answer=''
        for i in range(len(num)):
            answer+=str(num[i])
        return [int(i) for i in str(int(answer)+k)]