class Solution {
    public int titleToNumber(String columnTitle) {
        int n = columnTitle.length();
        int sum = 0;
        for(int i = 0; i < n; i++){
            sum *= 26;
            sum += columnTitle.charAt(i) - 'A' + 1;
        }
        return sum;
    }
}
