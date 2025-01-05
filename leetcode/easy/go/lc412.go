func fizzBuzz(n int) []string {
    result := make([]string, n)
    for i := 1; i <= n; i++ {
        var entry string
        if i%3 == 0 {
            entry += "Fizz"
        }
        if i%5 == 0 {
            entry += "Buzz"
        }
        if entry == "" {
            entry = fmt.Sprintf("%d", i)
        }
        result[i-1] = entry
    }
    return result
}

