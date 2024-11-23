class Solution {
    public boolean isPowerOfFour(int n) {
        if (n < 4) {
            return 1 == n;
        }
        while (n >= 4) {
            if (n % 4 == 0) {
                return isPowerOfFour(n / 4);
            }
            else {
                return false;
            }
        }
        return true;
    }
}

