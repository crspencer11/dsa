class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0 || matrix[0].length == 0) {
            return false;
        }
        int[] targetRow = findTargetArray(matrix, target);
        if (targetRow == null || targetRow.length == 0) {
            return false;
        }
        return bSearch(targetRow, target, 0, targetRow.length - 1);
    }
    
    private int[] findTargetArray(int[][] matrix, int target) {
        for (int i = 0; i < matrix.length; i++) {
            int[] row = matrix[i];
            if (row[0] <= target && target <= row[row.length - 1]) {
                return row;
            }
        }
        return null;
    }
    
    private boolean bSearch(int[] inputArray, int target, int low, int high) {
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (inputArray[mid] == target) {
                return true;
            }
            if (inputArray[mid] < target) {
                low = mid + 1;
            }
            else {
                high = mid - 1;
            }
        }
        return false;
    }
}

