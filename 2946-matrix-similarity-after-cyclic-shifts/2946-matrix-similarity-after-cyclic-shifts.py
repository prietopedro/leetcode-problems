class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        if not mat:
            return True

        n = len(mat[0])
        if k % n == 0:
            return True

        for row in range(len(mat)):
            for col in range(n):
                if mat[row][col] != mat[row][(col - k) % n]:
                    return False
        return True