import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> largeGroupPositions(String s) {
        List<List<Integer>> result = new ArrayList<>();
        int strLen = s.length();
        int j = 0; 
        
        for (int i = 1; i < strLen; i++) {
            if (s.charAt(i) != s.charAt(i - 1)) {
                if (i - j >= 3) {
                    List<Integer> group = new ArrayList<>();
                    group.add(j);
                    group.add(i - 1);
                    result.add(group);
                }
                j = i;
            }
        }
        
        if (strLen - j >= 3) {
            List<Integer> group = new ArrayList<>();
            group.add(j);
            group.add(strLen - 1);
            result.add(group);
        }
        return result;
    }
}

