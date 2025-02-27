func getConcatenation(nums []int) []int {
    ans := nums
    numsLen := len(nums)
    for i := 0; i < numsLen; i++ {
        ans = append(ans, nums[i])
    }
    return ans
}

