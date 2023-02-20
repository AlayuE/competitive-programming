class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0 
        fast = 1
        while fast < len(nums):
            if nums[slow]!=nums[fast]:
                nums[slow+1]=nums[fast]
                slow += 1
            else:
                fast += 1
        return slow + 1
                
                
            
        