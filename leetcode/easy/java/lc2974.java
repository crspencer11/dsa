class Solution {
    public int[] numberGame(int[] nums) {
        Arrays.sort(nums); 
        ArrayList<Integer> output = new ArrayList<>();

        for (int i = 0; i < nums.length / 2; i++) {
            output.add(nums[i]);
            output.add(nums[nums.length - 1 - i]);
        }

        if (nums.length % 2 != 0) {
            output.add(nums[nums.length / 2]);
        }

        int[] result = new int[output.size()];
        for (int i = 0; i < output.size(); i++) {
            result[i] = output.get(i);
        }
        return result;
    }
}

