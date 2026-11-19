class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_water = 0
        for height in heights:
            water = (r - l) * min(heights[l], heights[r])
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            max_water = max(water, max_water)
        return max_water