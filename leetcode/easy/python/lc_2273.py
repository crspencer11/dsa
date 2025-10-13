ass Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
            final = [words[0]]
	            for i in range(1, len(words)):
		                prev = words[i - 1]
				            curr = words[i]
					                if len(prev) == len(curr):
							                count = {}
									                for char in prev:
											                    count[char] = count.get(char, 0) + 1
													                    for char in curr:
															                        if char not in count:
																		                        count[char] = -1
																					                    else:
																							                            count[char] -= 1
																										                    is_anagram = True
																												                    for val in count.values():
																														                        if val != 0:
																																	                        is_anagram = False
																																				                        break
																																							            else:
																																								                    is_anagram = False
																																										                if not is_anagram:
																																												                final.append(curr)
																																														        return final

