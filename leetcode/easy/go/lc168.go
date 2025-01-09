func convertToTitle(columnNumber int) string {
	result := ""
	for columnNumber > 0 {
		columnNumber--
		remainder := columnNumber % 26
		result = string('A'+remainder) + result
		columnNumber /= 26
	}
	return result
}

