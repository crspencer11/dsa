class Solution {
    public int numberOfChild(int n, int k) {
        int children = n - 1;
        int rounds = k / children;
        int remaindner = k % children;
        if (rounds % 2 == 0) {
            return remaindner;
        }
        return children - remaindner;
    }
}

