class Solution {
    public int[] getConcatenation(int[] nums) {
        int numsLen = nums.length;
        int[] ans = new int[2 * numsLen];
        for (int i = 0; i < numsLen; i++) {
            ans[i] = nums[i];
            ans[i + numsLen] = nums[i];
        }
        return ans;
    }
}

