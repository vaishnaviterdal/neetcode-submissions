class Solution:
    def maxArea(self, heights: List[int]) -> int:
        high_water = 0
        left = 0
        right = len(heights)-1
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            water = width * height
            if high_water < water :
                high_water = water
                water = 0
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return high_water