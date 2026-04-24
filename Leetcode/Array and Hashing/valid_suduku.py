board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


def is_valid_sudoku(board):

    for r in range(9):
        hashset = set()

        for c in range(9):
            ch  = board[r][c]

            if ch != '.' and ch in hashset:
                return False

            hashset.add(ch)


    for c in range(9):
        hashset = set()

        for r in range(9):
            ch  = board[r][c]

            if ch != '.' and ch in hashset:
                return False

            hashset.add(ch)


    
    for box_row in range(3):
        for box_col in range(3):
            hashset = set()

            for r in range(3):
                for c in range(3):
                    ch = board[box_row * 3 + r][box_col * 3 + c]

                    if ch != '.' and ch in hashset:
                        return False

                    hashset.add(ch)


    return True


print(is_valid_sudoku(board))