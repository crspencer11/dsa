class Solution {
    public int maxAscendingSum(int[] nums) {
        int curr = nums[0];
        int total = curr;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i-1]) {
                curr += nums[i];
            }
            else {
                total = Math.max(total, curr);
                curr = nums[i];
            }
        }
        if (total > curr) {
            return total;
        }
        return curr;
    }
}

