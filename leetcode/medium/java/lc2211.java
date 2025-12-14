class Solution {
    public int countCollisions(String directions) {
        int left = 0;
        int right = directions.length() - 1;

        while (left <= right && directions.charAt(left) == 'L') {
            left++;
        }

        while (left <= right && directions.charAt(right) == 'R') {
            right--;
        }

        int collisions = 0;
        for (int i = left; i < right + 1; i++) {
            if (directions.charAt(i) != 'S') {
                collisions++;
            }
        }
        return collisions;
    }
}

