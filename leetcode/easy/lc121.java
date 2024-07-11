class Solution {
    public int maxProfit(int[] prices) {
        int maximum = 0;
        int minPrice = prices[0];
        for (int i=0; i<prices.length; i++) {
            maximum = Math.max(maximum, prices[i] - minPrice);
            minPrice = Math.min(minPrice, prices[i]);
        }
        return maximum;
    }
}
