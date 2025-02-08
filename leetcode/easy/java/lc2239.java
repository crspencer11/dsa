class Solution {
    public int findClosestNumber(int[] nums) {
        int firstDigit = nums[0];
        int closest = nums[0];
        int i = 0;
        while (i < nums.length) {
            int curr = Math.abs(nums[i]);
            if (curr < Math.abs(closest)) {
                closest = nums[i];
                firstDigit = nums[i];
            }
            if (curr == Math.abs(closest)) {
                closest = Math.max(nums[i], firstDigit);
            }
            i++;
        }
        return closest;
    }
}

