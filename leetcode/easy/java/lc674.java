class Solution {
    public int findLengthOfLCIS(int[] nums) {
        if (nums.length == 0) {
            return 0;
        } 
        else {
            int total = 1;
            int currMax = 1;
            for (int i = 1; i < nums.length; i++) {
                if (nums[i] > nums[i - 1]) {
                    currMax++;
                    if (currMax > total) {
                        total = currMax;
                    }
                } 
                else {
                    currMax = 1;
                }
            }
            return total;
        }
    }
}

