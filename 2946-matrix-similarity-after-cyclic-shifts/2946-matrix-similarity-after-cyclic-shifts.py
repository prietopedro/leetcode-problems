class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        if k == len(mat[0]):
            return True

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] != mat[row][(col - k) % len(mat[0])]:
                    return False
        return True