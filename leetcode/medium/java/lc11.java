class Solution {
    public int maxArea(int[] height) {
        int currMax = 0;
        int left = 0;
        int right = height.length - 1;
        while (left < right) {
            currMax = Math.max(currMax, (right - left) * Math.min(height[left], height[right]));
            if (height[left] < height[right]) {
                left++;
            }
            else {
                right--;
            }
        }
        return currMax;
    }
}
