class Solution {
    public int findClosest(int x, int y, int z) {
        int xDist = Math.abs(x - z);
        int yDist = Math.abs(y - z);
        if (xDist == yDist) {
            return 0;
        }
        if (xDist > yDist) {
            return 2;
        }
        return 1;
    }
}

