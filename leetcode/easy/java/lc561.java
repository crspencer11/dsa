class Solution {
    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);
        int total = 0;
        for (int i = nums.length - 2; i >= 0; i -= 2) {
            total += nums[i];
        }
        return total;
    }
}
