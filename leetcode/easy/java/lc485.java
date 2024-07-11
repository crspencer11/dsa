class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        int maxConsecutive = 0;
        int currentConsecutive = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                currentConsecutive++;
            } 
            else {
                if (currentConsecutive > maxConsecutive) {
                    maxConsecutive = currentConsecutive;
                }
                currentConsecutive = 0;
            }
        }
        if (currentConsecutive > maxConsecutive) {
            maxConsecutive = currentConsecutive;
        }
        return maxConsecutive;
    }
}

