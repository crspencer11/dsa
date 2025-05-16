class Solution {
    public List<String> getLongestSubsequence(String[] words, int[] groups) {
        List<String> res = new ArrayList<>();
        int end = -1;
        for (int i = 0; i < words.length; i++) {
            if (groups[i] != end) {
                res.add(words[i]);
                end = groups[i];
            }
        }
        return res;
    }
}
