class Solution {
    public int totalMoney(int n) {
        int weeks = n / 7;
        int days = n % 7;
        int total = 0;
        for (int w = 0; w < weeks; w++) {
            total += 28 + (7 * w);
        }
        for (int d = 0; d < days; d++) {
            total += (weeks + 1) + d;
        }
        return total;
    }
}

