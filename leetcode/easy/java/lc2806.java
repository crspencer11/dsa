class Solution {
    public int accountBalanceAfterPurchase(int purchaseAmount) {
        int baseTen = (purchaseAmount / 10) * 10;
        if (purchaseAmount < 10) {
            if (purchaseAmount >= 5) {
                return 90;
            }
            return 100 - baseTen;
        }
        if (purchaseAmount % 10 >= 5) {
            int subtract = baseTen + 10;
            return 100 - subtract;
        }
        return 100 - baseTen;
    }
}

