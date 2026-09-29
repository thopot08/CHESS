import pieces

class Board:
    def __init__(self):
        self.board = []
        self.clearBoard()

    def clearBoard(self): # recreates the board with no pieces on it
        self.board = []
        for _ in range(8):
            row = [0]*8
            self.board.append(row)

    def setDefaultPos(self):
        self.clearBoard()
        for i in range(8):
            # Pawns
            self.board[1][i] = pieces.Pawn("B","pawn", [1,i]) # black
            self.board[6][i] = pieces.Pawn("W","pawn", [6,i]) # white

            if i == 0 or i == 7: # rooks
                self.board[0][i] = pieces.Rook("B","rook",[0,i])
                self.board[7][i] = pieces.Rook("W","rook",[7,i])

            if i == 1 or i == 6: # knight
                self.board[0][i] = pieces.Knight("B","knight",[0,i])
                self.board[7][i] = pieces.Knight("W","knight",[7,i])

            if i == 2 or i == 5: # bishop
                self.board[0][i] = pieces.Bishop("B","bishop",[0,i])
                self.board[7][i] = pieces.Bishop("W","bishop",[7,i])

            if i == 3: # queen
                self.board[0][i] = pieces.Queen("B","queen",[0,i])
                self.board[7][i] = pieces.Queen("W","queen",[7,i])

            if i == 4: # king
                self.board[0][i] = pieces.King("B","king",[0,i])
                self.board[7][i] = pieces.King("W","king",[7,i])