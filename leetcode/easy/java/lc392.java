class Solution {
    public boolean isSubsequence(String s, String t) {
        int i = 0;
        int j = 0;
        int sLength = s.length();
        int tLength = t.length();
        while (i < sLength && j < tLength) {
            if (s.charAt(i) == t.charAt(j)) {
                i++;
            }
            j++;
        }
        if (i == sLength) {
            return true;
        }
        return false;
    }
}

