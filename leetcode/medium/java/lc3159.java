class Solution {
    public int[] occurrencesOfElement(int[] nums, int[] queries, int x) {
        HashMap<Integer, Integer> resultsMap = new HashMap<>();
        int count = 0;
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            if (nums[i] == x) {
                count++;
                resultsMap.put(count, i);
            }
        }
        for (int i = 0; i < queries.length; i++) {
            if (resultsMap.containsKey(queries[i])) {
                queries[i] = resultsMap.get(queries[i]);
            } else {
                queries[i] = -1;
            }
        }
        return queries;
    }
}

