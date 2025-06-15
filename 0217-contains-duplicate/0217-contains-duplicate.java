class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> hash = new HashSet<Integer>();
        for (int num : nums) hash.add(num);
        return hash.size() != nums.length;
    }
}