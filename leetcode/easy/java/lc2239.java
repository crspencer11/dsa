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

// bsearch impl
class Solution {
    public int findClosestNumber(int[] nums) {
        Arrays.sort(nums);
        int left = 0, right = nums.length - 1;
        int closest = nums[0];

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == 0) return 0; 
            if (Math.abs(nums[mid]) < Math.abs(closest) || 
                (Math.abs(nums[mid]) == Math.abs(closest) && nums[mid] > closest)) {
                closest = nums[mid];
            }
            if (nums[mid] < 0) {
                left = mid + 1; 
            } else {
                right = mid - 1; 
            }
        }
        return closest;
    }
}


