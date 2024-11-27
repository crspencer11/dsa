func letterCombinations(digits string) []string {
    if len(digits) == 0 {
        return []string{}
    }
    digitToLetters := map[byte]string{
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz",
    }
    var res []string
    var backtrack func(idx int, comb string)
    backtrack = func(idx int, comb string) {
        if idx == len(digits) {
            res = append(res, comb)
            return
        }
        letters := digitToLetters[digits[idx]]
        for i := 0; i < len(letters); i++ {
            backtrack(idx+1, comb+string(letters[i]))
        }
    }
    backtrack(0, "")
    return res
}

