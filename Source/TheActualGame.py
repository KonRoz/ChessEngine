import Pieces, Player, TheChessEngine

gameBoard = TheChessEngine.ChessBoard()

# white pawns

wp1 = Pieces.Pawn(input('please input a name for white Pawn #' + str(Pawn.white_piece_index + 1) + ': '),
           team=Colors.WHITE,
           location=(0, 1))
wp2 = Pawn(input('please input a name for white Pawn #' + str(Pawn.white_piece_index + 1) + ': '),
           team=Colors.WHITE,
           location=(1, 1))
wp3 = Pawn(input('please input a name for white Pawn #' + str(Pawn.white_piece_index + 1) + ': '),
           team=Colors.WHITE,
           location=(2, 1))
wp4 = Pawn(input('please input a name for white Pawn #' + str(Pawn.white_piece_index + 1) + ': '),
           team=Colors.WHITE,
           location=(3, 1))
wp5 = Pawn(input('please input a name for white Pawn #' + str(Pawn.white_piece_index + 1) + ': '),
           team=Colors.WHITE,
           location=(4, 1))
wp6 = Pawn(input('please input a name for white Pawn #' + str(Pawn.white_piece_index + 1) + ': '),
           team=Colors.WHITE,
           location=(5, 1))
wp7 = Pawn(input('please input a name for white Pawn #' + str(Pawn.white_piece_index + 1) + ': '),
           team=Colors.WHITE,
           location=(6, 1))
wp8 = Pawn(input('please input a name for white Pawn #' + str(Pawn.white_piece_index + 1) + ': '),
           team=Colors.WHITE,
           location=(7, 1))

# white rooks

wr1 = Rook(input('please input a name for white Rook #' + str(Rook.white_piece_index + 1) + ': '),
           team=Colors.WHITE,
           location=(0, 0))
wr2 = Rook(input('please input a name for white Rook #' + str(Rook.white_piece_index + 1) + ': '),
           team=Colors.WHITE,
           location=(7, 0))

# white knights

wk1 = Knight(input('please input a name for white Knight #' + str(Knight.white_piece_index + 1) + ': '),
             team=Colors.WHITE,
             location=(2, 0))
wk2 = Knight(input('please input a name for white Knight #' + str(Knight.white_piece_index + 1) + ': '),
             team=Colors.WHITE,
             location=(6, 0))

# white bishops

wb1 = Bishop(input('please input a name for white Bishop #' + str(Knight.white_piece_index + 1) + ': '),
             team=Colors.WHITE,
             location=(2, 0))
wb2 = Bishop(input('please input a name for white Bishop #' + str(Bishop.white_piece_index + 1) + '; '),
             team=Colors.BLACK,
             location=(5, 0))

# white King and Queen

wK = King(input('please input a name for white King #' + str(King.white_piece_index + 1) + ': '),
          team=Colors.WHITE,
          location=(3, 0))
wQ = Queen(input('please input a name for a white Queen #' + str(Queen.white_piece_index + 1) + ': '),
           team=Colors.WHITE,
           location=(4, 0))

# black pawns

bp1 = Pawn(input('please input a name for black Pawn #' + str(Pawn.black_piece_index + 1) + ': '),
           team=Colors.BLACK,
           location=(0, 6))
bp2 = Pawn(input('please input a name for black Pawn #' + str(Pawn.black_piece_index + 1) + ': '),
           team=Colors.BLACK,
           location=(1, 6))
bp3 = Pawn(input('please input a name for black Pawn #' + str(Pawn.black_piece_index + 1) + ': '),
           team=Colors.BLACK,
           location=(2, 6))
bp4 = Pawn(input('please input a name for black Pawn #' + str(Pawn.black_piece_index + 1) + ': '),
           team=Colors.BLACK,
           location=(3, 6))
bp5 = Pawn(input('please input a name for black Pawn #' + str(Pawn.black_piece_index + 1) + ': '),
           team=Colors.BLACK,
           location=(4, 6))
bp6 = Pawn(input('please input a name for black Pawn #' + str(Pawn.black_piece_index + 1) + ': '),
           team=Colors.BLACK,
           location=(5, 6))
bp7 = Pawn(input('please input a name for black Pawn #' + str(Pawn.black_piece_index + 1) + ': '),
           team=Colors.BLACK,
           location=(6, 6))
bp8 = Pawn(input('please input a name for black Pawn #' + str(Pawn.black_piece_index + 1) + ': '),
           team=Colors.BLACK,
           location=(7, 6))

# black rooks

br1 = Rook(input('please input a name for black Rook #' + str(Rook.black_piece_index + 1) + ': '),
           team=Colors.BLACK,
           location=(0, 7))
br2 = Rook(input('please input a name for black Rook #' + str(Rook.black_piece_index + 1) + ': '),
           team=Colors.BLACK,
           location=(7, 7))

# black knights

bk1 = Knight(input('please input a name for black Knight #' + str(Knight.black_piece_index + 1) + ': '),
             team=Colors.BLACK,
             location=(1, 7))
bk2 = Knight(input('please input a name for black Knight #' + str(Knight.black_piece_index + 1) + ': '),
             team=Colors.WHITE,
             location=(6, 7))

# black bishops

bb1 = Bishop(input('please input a name for black Bishop #' + str(Knight.black_piece_index + 1) + ': '),
             team=Colors.BLACK,
             location=(2, 7))
bb2 = Bishop(input('please input a name for black Bishop #' + str(Knight.black_piece_index + 1) + ': '),
             team=Colors.BLACK,
             location=(5, 7))

# black King and Queen

bK = King(input('please input a name for black King #' + str(King.black_piece_index + 1) + ': '),
          team=Colors.BLACK,
          location=(3, 7))
bQ = Queen(input('please input a name for a black Queen #' + str(Queen.black_piece_index + 1) + ': '),
           team=Colors.BLACK,
           location=(4, 7))

# adding white pieces to the board
gameBoard.add_pieces(wp1, wp2, wp3, wp4, wp5, wp6, wp7, wp8, wr1, wr2, wk1, wk2, wb1, wb2, wK, wQ)

# adding black pieces to the board
gameBoard.add_pieces(bp1, bp2, bp3, bp4, bp5, bp6, bp7, bp8, br1, br2, bk1, bk2, bb1, bb2, bK, bQ)

gameBoard.display_board()