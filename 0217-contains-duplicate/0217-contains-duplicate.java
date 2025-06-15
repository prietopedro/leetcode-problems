class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> uniqueElements = Arrays.stream(nums)
                                            .boxed()
                                            .collect(Collectors.toSet());
        return uniqueElements.size() != nums.length;
    }
}