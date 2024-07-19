class Solution {
    public int mySqrt(int x) {
        if (x == 0) {
            return 0;
        }
        int first = 1;
        int last = x;
        while (first <= last) {
            int mid = first + (last - first) / 2;
            if (mid == x / mid) {
                return mid;
            }
            if (mid > x / mid) {
                last = mid - 1;
            } 
            else {
                first = mid + 1;
            }
        }
        return last;
    }
}
