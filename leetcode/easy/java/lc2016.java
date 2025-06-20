class Solution {
    public int maximumDifference(int[] nums) {
        int currMin = nums[0];
        int maxDiff = -1;

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > currMin) {
                maxDiff = Math.max(maxDiff, nums[i] - currMin);
            } else {
                currMin = nums[i];
            }
        }
        return maxDiff;
    }
}

