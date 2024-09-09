class Solution {
    public int firstUniqChar(String s) {
        Map<Character, Integer> charMap = new HashMap<>();
        int stringLen = s.length();
        for (int i=0; i<stringLen; i++) {
            char c = s.charAt(i);
            charMap.put(c, charMap.getOrDefault(c, 0) + 1);
        }

        for (int j=0; j<stringLen; j++) {
            if (charMap.get(s.charAt(j)) == 1) {
                return j;
            }
        }
        return -1; 
    }
}

