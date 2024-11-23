func arrangeCoins(n int) int {
    k := 0
    for i := 1; n >= i; i++ {
        n -= i
        k++
    }
    return k
}

