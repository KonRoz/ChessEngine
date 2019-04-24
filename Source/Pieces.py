class Color:
    WHITE = True
    BLACK = False


class Pieces:

    # to help determine if the # of pieces is correct
    white_piece_index = 0
    black_piece_index = 0
    piece_names = []

    # every piece on the board with will have the following properties
    def __init__(self, short_name=None, *, team=None, location=None):
        self.team = team
        self.location = location
        self.never_moved = True
        self.status = True
        self.short_name = short_name

    # every piece will be able to move
    def move(self, to_space):
        self.location = to_space


class Pawn(Pieces):

    def __init__(self, short_name, team, **kwargs):

        # assign short name by which the given piece can be referenced in the future
        if team is Color.WHITE:
            self.short_name = short_name if short_name not in Pieces.piece_names else + 'WP' + str(Pawn.white_piece_index)
            Pawn.white_piece_index += 1

        elif team is Color.BLACK:
            self.short_name = short_name if short_name not in Pieces.piece_names else + 'BP' + str(Pawn.black_piece_index)
            Pawn.black_piece_index += 1

        Pieces.piece_names.append(self.short_name)
        super().__init__(self.short_name, **kwargs)

    def output_moves(self, boardayout):
        # pawn can only move forward
        if boardayout[0]
        print(self.location[1]+1)


    def move(self):
        pass


class Rook(Pieces):

    def __init__(self, short_name, team, **kwargs):

        if team is Color.WHITE:
            self.short_name = short_name if short_name not in Pieces.piece_names else str(Color.WHITE) + 'Rook' + str(Rook.white_piece_index)
            Rook.white_piece_index += 1

        elif team is Color.BLACK:
            self.short_name = short_name if short_name not in Pieces.piece_names else str(Color.BLACK) + 'Rook' + str(Rook.black_piece_index)
            Rook.black_piece_index += 1

        Pieces.piece_names.append(self.short_name)
        super().__init__(self.short_name, **kwargs)

    def move(self):
        pass



class Knight(Pieces):

    def __init__(self, short_name, team, **kwargs):

        if team is Color.WHITE:
            self.short_name = short_name if short_name not in Pieces.piece_names else str(Color.WHITE) + 'Knight' + str(Knight.white_piece_index)
            Knight.white_piece_index += 1

        elif team is Color.BLACK:
            self.short_name = short_name if short_name not in Pieces.piece_names else str(Color.BLACK) + 'Knight' + str(Knight.black_piece_index)
            Knight.black_piece_index += 1

        Pieces.piece_names.append(self.short_name)
        super().__init__(self.short_name, **kwargs)

    def move(self):
        pass


class Bishop(Pieces):

    def __init__(self, short_name, team, **kwargs):

        if team is Color.WHITE:
            self.short_name = short_name if short_name not in Pieces.piece_names else str(Color.WHITE) + 'Bishop' + str(Bishop.white_piece_index)
            Bishop.white_piece_index += 1

        elif team is Color.BLACK:
            self.short_name = short_name if short_name not in Pieces.piece_names else str(Color.BLACK) + 'Bishop' + str(Bishop.black_piece_index)
            Bishop.black_piece_index += 1

        Pieces.piece_names.append(self.short_name)
        super().__init__(self.short_name, **kwargs)

    def move(self):
        pass


class Queen(Pieces):
    def __init__(self, short_name, team, **kwargs):

        if team is Color.WHITE:
            self.short_name = short_name if short_name not in Pieces.piece_names else str(Color.WHITE) + 'Queen' + str(Queen.white_piece_index)
            Bishop.white_piece_index += 1

        elif team is Color.BLACK:
            self.short_name = short_name if short_name not in Pieces.piece_names else str(Color.BLACK) + 'Queen' + str(Queen.black_piece_index)
            Queen.black_piece_index += 1

        Pieces.piece_names.append(self.short_name)
        super().__init__(self.short_name, **kwargs)

    def move(self):
        pass


class King(Pieces):
    def __init__(self, short_name, team, **kwargs):

        if team is Color.WHITE:
            self.short_name = short_name if short_name not in Pieces.piece_names else str(Color.WHITE) + 'King' + str(King.white_piece_index)
            King.white_piece_index += 1

        elif team is Color.BLACK:
            self.short_name = short_name if short_name not in Pieces.piece_names else str(Color.BLACK) + 'King' + str(King.black_piece_index)
            King.black_piece_index += 1

        Pieces.piece_names.append(self.short_name)
        super().__init__(self.short_name, **kwargs)

    def move(self):
        pass