class Solution {
    public int trap(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int leftMax, rightMax, maxArea;
        leftMax = rightMax = maxArea = 0;
        while (left < right) {
            if (height[left] < height[right]) {
                if (height[left] >= leftMax) {
                    leftMax = height[left];
                } else {
                    maxArea += leftMax - height[left];
                }
                left++;
            } else {
                if (height[right] >= rightMax) {
                    rightMax = height[right];
                } else {
                    maxArea += rightMax - height[right];
                }
                right--;
            }
        }
        return maxArea;
    }
}
