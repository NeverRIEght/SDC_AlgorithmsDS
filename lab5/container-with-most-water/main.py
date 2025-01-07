class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two pointers
        # O(n), where n is the number of heights

        left_border = 0
        right_border = len(height) - 1
        max_area = 0

        while left_border < right_border:
            # Area as a minimum of two heights * width
            current_area = min(height[left_border], height[right_border]) * (right_border - left_border)

            # Is it bigger than previous max area?
            max_area = max(max_area, current_area)

            # Move the pointer that has the smaller height
            if height[left_border] < height[right_border]:
                left_border += 1
            else:
                right_border -= 1

        return max_area