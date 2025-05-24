class Solution {
    public String triangleType(int[] num) {
        if(num[0]+num[1] <= num[2] || num[1]+num[2] <= num[0] || num[0]+num[2] <= num[1]){
            return "none"; 
        }
        if(num[0]==num[1] && num[1]==num[2]){
            return "equilateral";
        }
        if(num[0]==num[1] || num[1]==num[2] || num[2]==num[0]){
            return "isosceles";   
        }
        else{
            return "scalene";
        }
    }
}

