class Solution {
    public boolean judgeCircle(String moves) {
        int horizontal = 0;
        int vertical = 0;
        for (int i = 0; i < moves.length(); i++) {
            char move = moves.charAt(i);
            if (move == 'L') {
                horizontal--;
            } else if (move == 'R') {
                horizontal++;
            } else if (move == 'U') {
                vertical++;
            } else if (move == 'D') {
                vertical--;
            }
        }
        return horizontal == 0 && vertical == 0;
    }
}

