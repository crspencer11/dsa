func twoSum(nums []int, target int) []int {
    myMap := make(map[int]int)
    for i, val := range nums {
        remainder := target - val
        if index, exists := myMap[remainder]; exists {
            return []int{index, i}
        }
        myMap[val] = i 
    }
    return nil
}

