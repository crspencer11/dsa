class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> results = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        backtrack(nums, new ArrayList<>(), used, results);
        return results;
    }

    private void backtrack(int[] nums, List<Integer> permutation, boolean[] used, List<List<Integer>> results) {
        if (permutation.size() == nums.length) {
            results.add(new ArrayList<>(permutation));
            return;
        }
        else {
            for (int i=0; i<nums.length; i++) {
                if (!used[i]) {
                    used[i] = true;
                    permutation.add(nums[i]);
                    backtrack(nums, permutation, used, results);
                    permutation.remove(permutation.size() - 1);
                    used[i] = false;
                }
            }
        }
    }
}
