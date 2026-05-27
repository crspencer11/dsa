class DynamicArray {
    private int[] arr;
    private int capacity;
    private int length;

    public DynamicArray(int capacity) {
        this.capacity = capacity;
        this.length = 0;
        this.arr = new int[capacity]; 
    }

    public int get(int i) {
        return this.arr[i];
    }

    public void set(int i, int n) {
        this.arr[i] = n;
    }

    public void pushback(int n) {
        if (this.length == this.capacity) {
            this.resize();
        }
        this.arr[this.length] = n;
        this.length++;
    }

    public int popback() {
        int val = this.arr[this.length - 1];
        this.length--;
        return val;
    }

    private void resize() {
        this.capacity = 2 * this.capacity;
        int[] copiedArr = new int[this.capacity]; 
        for (int i = 0; i < this.length; i++) {
            copiedArr[i] = this.arr[i];
        }
        this.arr = copiedArr;
    }

    public int getSize() {
        return this.length;
    }

    public int getCapacity() {
        return this.capacity;
    }
}
