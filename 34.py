class Solution:
    def isValidSudoku(self, board) -> bool:

        dd = ['1','2','3','4','5','6','7','8','9']
        for i in range(9):
            tt = {}
            for j in range(9):
                if board[i][j] in tt.keys() and board[i][j] != '.':
                    return False
                else:
                    tt[board[i][j]] = 1
        for j in range(9):
            tt = {}
            for i in range(9):
                if board[i][j] in tt.keys() and board[i][j] != '.':
                    return False
                else:
                    tt[board[i][j]] = 1

        for i in range(9):
            tt = {}
            for j in range(9):
                if board[3*(i//3)+j//3][(i%3)*3+j%3] in tt.keys() and board[3*(i//3)+j//3][(i%3)*3+j%3] != '.':
                    return False
                else:
                    tt[board[3*(i//3)+j//3][(i%3)*3+j%3]] = 1
        return True





