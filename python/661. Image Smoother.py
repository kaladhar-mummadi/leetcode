import copy
class Solution(object):
    def brute_force(self, M, row_x, col_y):
        positions = [(0,1), (1,0), (0,-1), (-1, 0), (1,1), (-1,-1), (1,-1), (-1,1)]
        considered = 1
        surround_sum = M[row_x][col_y]
        for pos in positions:
            i,j = row_x+pos[0],col_y+pos[1]

            if i < 0 or j < 0 or i >= len(M) or j >= len(M[0]):
                continue
            surround_sum += M[i][j]
            considered += 1

        return surround_sum // considered


    def imageSmoother(self, M):
        M_copy = copy.deepcopy(M)

        for i in range(len(M)):
            for j in range(len(M[0])):
                M[i][j] = self.brute_force(M_copy,i,j)
        return M

sol = Solution()
print(sol.imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))