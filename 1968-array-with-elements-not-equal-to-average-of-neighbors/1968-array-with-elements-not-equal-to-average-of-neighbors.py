class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = []
        nums.sort()
        left,right = 0,len(nums)-1
        while len(ans) != len(nums):
            ans.append(nums[left])
            left += 1
            if left <= right:
                ans.append(nums[right])
                right -= 1
        return ans
        