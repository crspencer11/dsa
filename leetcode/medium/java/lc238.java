class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] result = new int[nums.length];
        int pre = 1;
        for (int i = 0; i < nums.length; i++) {
            result[i] = pre;
            pre *= nums[i];
        }

        int post = 1;
        int j = nums.length - 1;
        while (j >= 0) {
            result[j] *= post;
            post *= nums[j];
            j--;
        }
        return result;
    }
}
