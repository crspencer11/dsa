class Main {
  static int linearSearch(int[] nums, int target) {
    int size = nums.length;

    for (int i=0; i < size; i++) {
      if (nums[i] == target) {
        System.out.println("Target Value found @ index " + i);
	return i;
      }
    }
    System.out.println("Value does not exist in array!");
    return -1;
  }
 
   public static void main(String args[]) {
     int[] data = {13, 0, 8, -14};
     int target = 8;
     Main.linearSearch(data, target);
  }
}
