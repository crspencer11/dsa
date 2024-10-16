class Main {
  static void bubbleSort(int[] nums) {
    int size = nums.length;

    for(int i=0; i<(size-1); i++) {
      for(int j=0; j<(size-i-1); j++) {
        if(nums[j] > nums[j+1]) {
	  int temp = nums[j];
	  nums[j] = nums[j+1];
	  nums[j+1] = temp;
	}
      }
    }
  }

  public static void main(String args[]) {
    int[] data = {5, -4, 16, 1, 28};
    Main.bubbleSort(data);
    System.out.println(data);
  }
}
