
func getRow(n int) []int {
    if n == 0 {
        return []int{1}
    }
    dp := []int{1}
    for i := 1; i <= n; i++ {
        temp := make([]int, i+1)
        temp[0], temp[i] = 1, 1
        for j := 1; j < i; j++ {
            temp[j] = dp[j-1] + dp[j]
        }
        dp = temp
    }
    return dp
}
