public class Solution {
    public int search(int[] nums, int target) {
        return bSearch(nums, target, 0, nums.length - 1);
    }

    private int bSearch(int[] nums, int target, int first, int last) {
        if (first > last) {
            return -1;
        }
        int mid = (first + last) / 2;
        if (nums[mid] == target) {
            return mid;
        }
        if (nums[first] <= nums[mid]) {
            if (nums[first] <= target && target <= nums[mid]) {
                return bSearch(nums, target, first, mid - 1);
            } 
            return bSearch(nums, target, mid + 1, last);
        } 
        else {
            if (nums[mid] <= target && target <= nums[last]) {
                return bSearch(nums, target, mid + 1, last);
            } 
            return bSearch(nums, target, first, mid - 1);
        }
    }
}

