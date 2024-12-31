class Solution {
    public int numberOfAlternatingGroups(int[] colors) {
        int totalGroups = 0;
        int n = colors.length;
        int i = 0;
        int left = n - 1;
        int right = 1;

        while (i < n) {
            if (colors[i] != colors[left] && colors[i] != colors[right]) {
                totalGroups++;
            }
            left = i; 
            right = (i + 2) % n;
            i++;
        }
        return totalGroups;
    }
}

