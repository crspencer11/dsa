class Solution {
    public int smallestNumber(int n, int t) {
        for (int i = n; i < n + 10; i++) {
            if (findProduct(i) % t == 0) {
                return i;
            }
        }
        return -1;
    }
    private int findProduct(int x) {
        int product = 1;
        while (x >= 1) {
            product *= x % 10;
            x /= 10;
        }
        return product;
    }
}

