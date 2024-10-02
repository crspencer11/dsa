class Solution {
    public int distanceBetweenBusStops(int[] distance, int start, int destination) {
        int firstBus = 0;
        int secondBus = 0;
        for (int i=0; i<distance.length; i++){
            if (start <= i && i < destination || start > i && i >= destination) {
                firstBus += distance[i];
            }
            else {
                secondBus += distance[i];
            }
        }
        if (firstBus > secondBus) {
            return secondBus;
        }
        return firstBus;
    }
}
