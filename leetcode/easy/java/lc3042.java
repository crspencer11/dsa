class Solution {
    public int countPrefixSuffixPairs(String[] words) {
        int n = words.length;
        int count = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (isPrefixAndSuffix(words[i], words[j])) {
                    count++;
                }
            }
        }
        return count;
    }

    private boolean isPrefixAndSuffix(String str1, String str2) {
        int str1Length = str1.length();
        int str2Length = str2.length();
        if (str1Length > str2Length) {
            return false;
        }
        for (int i = 0; i < str1Length; ++i) {
            if (str1.charAt(i) != str2.charAt(i) || 
                str1.charAt(str1Length - i - 1) != str2.charAt(str2Length - i - 1)) {
                return false;
            }
        }
        return true;
    }
}

