#import Source.Pieces


class ChessBoard:

    def __init__(self):
        # creating a dictionary that will hold a tuple for the coordinates and a value slot for a piece
        self.board = {}
        for x in range(8):
            for y in range(8):
                self.board[(x, y)] = None

    def list_positions(self):
        for my in range(8):
            for mx in range(8):
                if self.board[(mx, my)] is not None:
                    print( self.board[(mx, my)].short_name, ' at:', '( x coor: ', mx,
                         ', y coor: ', my, ' )')
                    print('Piece')
                else:
                    print('NONE', ' at:', '( x coor: ', mx, ', y coor: ', my, ' )')

    def display_board(self):
        for my in range(8):
            for mx in range(8):
                if self.board[(mx, my)] is not None and mx != 7:
                    print(" . ", end="", flush=True)
                elif self.board[(mx, my)] is not None and mx == 7:
                    print(' . ')
                elif self.board[(mx, my)] is None and mx != 7:
                    print(" - ", end="", flush=True)
                elif self.board[(mx, my)] is None and mx == 7:
                    print(' - ')

    def set_up_board(self):
        pass

    def add_or_deleter_piece(self, PieceType, action, locaction):
        if action is 'kill':
            pass
        elif action is 'add':
            pass
        else:
            pass


TestBoard = ChessBoard()
TestBoard.display_board()
