class Solution {
    public int maxPower(String s) {
        int globMax = 1;
        int currMax = 1;
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == s.charAt(i - 1)) {
                currMax++;
            } else {
                currMax = 1;
            }
            globMax = Math.max(globMax, currMax);
        }
        return globMax;
    }
}

