class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> result = new ArrayList<>();
        int maxCandies = 0;
        for (int candy : candies) {
            if (candy > maxCandies) {
                maxCandies = candy;
            }
        }
        for (int candy : candies) {
            if (candy + extraCandies >= maxCandies) {
                result.add(true);
            } 
            else {
                result.add(false);
            }
        }
        
        return result;
    }
}

