import Pieces

class ChessBoard:

    def __init__(self):
        # creating a dictionary that will hold a tuple for the coordinates and a value slot for a piece
        self.board = {}
        for x in range(8):
            for y in range(8):
                self.board[(x, y)] = None

    def display_board(self):
        for my in range(8):
            for mx in range(8):
                if self.board[(mx, my)] is not None:
                    print( self.board[(mx, my)].short_name, ' at:', '( x coor: ', mx,
                          ', y coor: ', my, ' )')
                else:
                    print('NONE', ' at:', '( x coor: ', mx, ', y coor: ', my, ' )')
    def set_up_board(self):
        Pieces.Pawn(team=True, )

    def add_pieces(self):
        pass

