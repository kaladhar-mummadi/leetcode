class Solution(object):
    def move_right(self,matrix, i, columns, level, res):
        moved = False
        for j in range(level, columns-level):
            res.append(matrix[i][j])
            moved = True
        return moved

    def move_down(self, matrix, j, rows, level, res):
        moved = False
        for i in range(level+1, rows-level):
            res.append(matrix[i][j])
            moved = True
        return moved

    def move_left(self, matrix, i, columns, level, res):
        moved = False
        for j in range(columns-level-1, level-1, -1):
            res.append(matrix[i][j])
            moved = True
        return moved
    def move_up(self, matrix, j , rows, level, res):
        moved = False
        for i in range(rows-level-1, level, -1):
            res.append(matrix[i][j])
            moved = True
        return moved

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if len(matrix) == 0:
            return res
        can_rotate = min(len(matrix), len(matrix[0]))
        columns = len(matrix[0])
        rows = len(matrix)
        level = 0
        while can_rotate > 0:
            if not self.move_right(matrix, level, columns, level, res):
                break
            if not self.move_down(matrix, columns-level-1, rows, level, res):
                break
            if not self.move_left(matrix, rows-level-1, columns-1, level, res):
                break
            if not self.move_up(matrix, level, rows-1, level, res):
                break
            can_rotate -= 2
            level += 1
        return res


sol = Solution()
print(sol.spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]))