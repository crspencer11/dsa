func canAliceWin(nums []int) bool {
    n := 0
    sum := 0
    for i := 0; i < len(nums); i++ {
        if nums[i] <= 9 {
            n += nums[i]
        } else {
            sum += nums[i]
        }
    }
    if sum == n {
        return false
    } else {
        return true
    }
}
