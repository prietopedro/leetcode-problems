class Solution {
    public boolean threeConsecutiveOdds(int[] arr) {
        var counter = 0;
        for (var num : arr){
            if (num % 2 == 0) counter = 0;
            else counter += 1;
            if (counter == 3) return true;
        }
        return false;
    }
}