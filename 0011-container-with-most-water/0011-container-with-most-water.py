class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        volume = 0
        while right > left:
            min_l = min(height[left],height[right])
            volume_l = min_l * (right -left)
            volume = max(volume, volume_l)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return volume
        