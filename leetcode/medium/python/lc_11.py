class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            if height[left] > height[right]:
                top = height[right]
            else:
                top = height[left]
            new = (right - left) * top
            if max_area < new:
                max_area = new
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return max_area
