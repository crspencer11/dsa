class Solution {
    public String gcdOfStrings(String str1, String str2) {
        if (!(str1 + str2).equals(str2 + str1)) {
            return "";
        }
        int lenGCD = findGCD(str1.length(), str2.length());
        return str1.substring(0, lenGCD);        
    }

    private int findGCD(int str1Len, int str2Len) {
        while (str2Len != 0) {
            int tempLen = str1Len % str2Len;
            str1Len = str2Len;
            str2Len = tempLen;
        }
        return str1Len;
    }
}

