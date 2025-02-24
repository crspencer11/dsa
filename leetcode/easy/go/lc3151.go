func isArraySpecial(nums []int) bool {
    nums_len := len(nums)
    if nums_len == 1 {
        return true
    }
    i := 0
    j := 1
    for j < nums_len {
        if nums[i] % 2 == 0 && nums[j] % 2 == 0 {
            return false
        }
        if nums[i] % 2 != 0 && nums[j] % 2 != 0 {
            return false
        }
        i += 1
        j += 1
    }
    return true
}

