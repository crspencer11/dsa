func isPrefixOfWord(sentence string, searchWord string) int {
    words := strings.Split(sentence, " ")
	searchLen := len(searchWord)
	for i, word := range words {
		if len(word) >= searchLen && word[:searchLen] == searchWord {
			return i + 1
		}
	}
	return -1
}

