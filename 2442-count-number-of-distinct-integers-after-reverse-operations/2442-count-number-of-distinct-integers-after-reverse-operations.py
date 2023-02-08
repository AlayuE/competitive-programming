class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        output = set([item for item in nums])
        for item in nums:
            output.add(int(str(item)[::-1]))
        return len(output)
        