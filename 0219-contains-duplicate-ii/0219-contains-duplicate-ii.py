class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        arrays=set()
        for i in range(len(nums)):
            if nums[i] in arrays:
                return True
            arrays.add(nums[i])
            if len(arrays)>k:
                arrays.remove(nums[i-k])
        return False