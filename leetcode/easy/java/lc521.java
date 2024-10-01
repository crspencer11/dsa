class Solution {
    public int findLUSlength(String a, String b)
    {
        int aLength = a.length();
        int bLength = b.length();
        if(a.equals(b)){
            return -1;
        }
        else{
            if (aLength > bLength){
                return aLength;
            }
            return bLength;
        }
        
    }
}

