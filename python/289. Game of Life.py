import copy
class Solution(object):
    def can_live(self,board,i,j, rows, columns):
        ans = 0
        #left
        if j-1 >= 0 and board[i][j-1]:
            ans += 1
        #up
        if i-1 >= 0 and board[i-1][j]:
            ans += 1
        #right
        if j+1 < columns and board[i][j+1]:
            ans += 1

        #down
        if  i+1 < rows and board[i+1][j]:
            ans += 1

        #top-left
        if i-1 >= 0 and j-1>=0 and board[i-1][j-1]:
            ans += 1
        #top-right
        if i-1 >=0 and j+1 < columns and board[i-1][j+1]:
            ans += 1

        #bottom-right

        if i + 1 < rows and j+1 < columns and board[i+1][j+1]:
            ans += 1

        #bottom left
        if i + 1 < rows and j - 1 >= 0 and board[i+1][j-1]:
            ans += 1

        if ans == 3 and board[i][j] == 0:
            return 1
        if board[i][j]:
            if ans > 3 or ans < 2:
                return 0
            elif board[i][j]:
                return 1

        return 0



    def brute_force(self, board):
        new_board = copy.deepcopy(board)

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = self.can_live(new_board, i,j,len(board), len(board[0]))

        # return new_board

    def gameOfLife(self, board):

        self.brute_force(board)

sol = Solution()
print(sol.brute_force([
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]))

