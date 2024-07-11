class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        else {
            int copy = x;
            int reversed = 0;
            while (copy > 0) {
                reversed = (reversed * 10) + (copy % 10);
                copy /= 10;
            }
            return reversed == x;
        }
    }
}

