public class Solution {
    public String longestPalindrome(String s) {
        int n = s.length();
        String longest = "";
        if (n == 0) {
            return longest;
        }

        for (int i = 0; i < n; i++) {
            int oddLeft = i;
            int oddRight = i;
            while (oddLeft >= 0 && oddRight < n && s.charAt(oddLeft) == s.charAt(oddRight)) {
                if (oddRight - oddLeft + 1 > longest.length()) {
                    longest = s.substring(oddLeft, oddRight + 1);
                }
                oddLeft--;
                oddRight++;
            }

            // Check for even-length palindromes centered at i and i+1
            int evenLeft = i, evenRight = i + 1;
            while (evenLeft >= 0 && evenRight < n && s.charAt(evenLeft) == s.charAt(evenRight)) {
                if (evenRight - evenLeft + 1 > longest.length()) {
                    longest = s.substring(evenLeft, evenRight + 1);
                }
                evenLeft--;
                evenRight++;
            }
        }
        return longest;
    }
}

