class Solution(object):
    def checkTwoChessboards(self, coordinate1, coordinate2):
        """
        :type coordinate1: str
        :type coordinate2: str
        :rtype: bool
        """
        letters_map = {
            "a": 1,
            "b": 2,
            "c": 3,
            "d": 4,
            "e": 5,
            "f": 6,
            "g": 7,
            "h": 8
        }
        first_col = letters_map[coordinate1[0]]
        first_row = int(coordinate1[1])
        second_col = letters_map[coordinate2[0]]
        second_row = int(coordinate2[1])
        
        return (first_col + first_row) % 2 == (second_col + second_row) % 2 

