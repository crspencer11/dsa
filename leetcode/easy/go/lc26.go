func removeDuplicates(nums []int) int {
    j := 0
    numsLen := len(nums)
    for i := 0; i < numsLen; i++ {
        if nums[i] != nums[j] {
            j++;
            nums[j] = nums[i]
        }
    }
    return j+1
}

