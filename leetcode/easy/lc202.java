class Solution {
    public boolean isHappy(int n) {
        if (n < 10) {
            return (n == 1 || n == 7);
        }
        else {
            int total = 0;
            while (n > 0) {
                total += (n%10) * (n%10);
                n /= 10;
            }
            return isHappy(total);
        }
    }
}
