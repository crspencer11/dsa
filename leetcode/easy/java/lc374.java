public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int first = 1;
        int last = n;
        while (first <= last) {
            int mid = first + (last - first) / 2;
            int result = guess(mid);
            if (result == 0) {
                return mid;
            }
            if (result == -1) {
                last = mid - 1;
            } 
            else {
                first = mid + 1;
            }
        }
        return -1;
    }
}
