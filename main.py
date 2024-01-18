# container with most water
# You are given an integer array height of length n. There are n vertical lines drawn
# such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container
# contains the most water.

# first solution is we could use bruteforce like this, but the time complexity is O(n ** 2)
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        for l in range(len(height)):
            for r in range(l + 1, len(height)):
                area = (r - l) * min(height[l], height[r])
                res = max(res, area)
        return res

# a better solution is this one, with a time complexity of O(n)
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        l = 0
        r = len(height)
        while r > l:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            if l >= r:
                r -= 1:
            else:
                l += 1
        return res