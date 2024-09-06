class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] splitStr = s.split(" ");
        int patternLen = pattern.length();

        if (patternLen != splitStr.length) {
            return false;
        }

        HashMap<Character, String> tracker = new HashMap<>();
        HashMap<String, Character> reverseTracker = new HashMap<>();

        for (int i = 0; i < patternLen; i++) {
            char currentChar = pattern.charAt(i);
            String currentWord = splitStr[i];

            if (!tracker.containsKey(currentChar)) {
                if (reverseTracker.containsKey(currentWord)) {
                    return false;
                }
                tracker.put(currentChar, currentWord);
                reverseTracker.put(currentWord, currentChar);
            } else {
                if (!tracker.get(currentChar).equals(currentWord)) {
                    return false;
                }
            }
        }
        return true;
    }
}

