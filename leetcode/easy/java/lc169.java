class Solution {
    public int majorityElement(int[] nums) {
        int selectedInt = nums[0];  
        int count = 1;
        for (int i = 1; i < nums.length; i++) {
            if (count == 0) {
                selectedInt = nums[i];
                count = 1;
            } 
            else if (nums[i] == selectedInt) {
                count++;
            } 
            else {
                count--;
            }
        }
        return selectedInt;
    }
}

