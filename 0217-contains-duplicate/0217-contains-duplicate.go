func containsDuplicate(nums []int) bool {
    seen := make(map[int]struct{})
    for _,num := range nums {
        _,contains := seen[num]
        if contains {
            return true
        }
        seen[num] = struct{}{}
    }
    return false
}