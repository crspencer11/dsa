func maxProfit(prices []int) int {
    if len(prices) == 0 {
        return 0
    }
    currMin := prices[0]
    maxProfit := 0
    for i := 1; i < len(prices); i++ {
        if prices[i] < currMin {
            currMin = prices[i]
        } else {
            profit := prices[i] - currMin
            if profit > maxProfit {
                maxProfit = profit
            }
        }
    }
    return maxProfit
}

