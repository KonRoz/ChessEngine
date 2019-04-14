import ABC


class Pieces(ABC):
    white_piece_index = 0
    black_piece_index = 0
    piece_names = []

    def __init__(self, short_name=None, *, team=None, location=None):
        self.team = team
        self.location = location
        self.never_moved = True
        self.status = True
        self.short_name = short_name

        super().__init__()

    @abstractmethod
    def move(self, Icoordinates, Fcoordinates):
        pass


class Pawn(Pieces):

    def __init__(self, short_name, team, **kwargs):

        if team is Colors.WHITE:
            self.short_name = short_name if short_name not in Pieces.piece_names else str(Colors.WHITE.name) + 'Pawn' + str(Pawn.white_piece_index)
            Pawn.white_piece_index += 1

        elif team is Colors.BLACK:
            self.short_name = short_name if short_name not in Pieces.piece_names else str(Colors.BLACK.name) + 'Pawn' + str(Pawn.black_piece_index)
            Pawn.black_piece_index += 1

        Pieces.piece_names.append(self.short_name)
        super().__init__(self.short_name, **kwargs)

    def move(self):
        pass


class Rook(Pieces):

    def __init__(self, short_name, team, **kwargs):

        if team is Colors.WHITE:
            self.short_name = short_name if short_name not in Pieces.piece_names else str(Colors.WHITE.name) + 'Rook' + str(Rook.white_piece_index)
            Rook.white_piece_index += 1

        elif team is Colors.BLACK:
            self.short_name = short_name if short_name not in Pieces.piece_names else str(Colors.BLACK.name) + 'Rook' + str(Rook.black_piece_index)
            Rook.black_piece_index += 1

        Pieces.piece_names.append(self.short_name)
        super().__init__(self.short_name, **kwargs)

    def move(self):
        pass


class Knight(Pieces):

    def __init__(self, short_name, team, **kwargs):

        if team is Colors.WHITE:
            self.short_name = short_name if short_name not in Pieces.piece_names else str(Colors.WHITE.name) + 'Knight' + str(Knight.white_piece_index)
            Knight.white_piece_index += 1

        elif team is Colors.BLACK:
            self.short_name = short_name if short_name not in Pieces.piece_names else str(Colors.BLACK.name) + 'Knight' + str(Knight.black_piece_index)
            Knight.black_piece_index += 1

        Pieces.piece_names.append(self.short_name)
        super().__init__(self.short_name, **kwargs)

    def move(self):
        pass


class Bishop(Pieces):

    def __init__(self, short_name, team, **kwargs):

        if team is Colors.WHITE:
            self.short_name = short_name if short_name not in Pieces.piece_names else str(Colors.WHITE.name) + 'Bishop' + str(Bishop.white_piece_index)
            Bishop.white_piece_index += 1

        elif team is Colors.BLACK:
            self.short_name = short_name if short_name not in Pieces.piece_names else str(Colors.BLACK.name) + 'Bishop' + str(Bishop.black_piece_index)
            Bishop.black_piece_index += 1

        Pieces.piece_names.append(self.short_name)
        super().__init__(self.short_name, **kwargs)

    def move(self):
        pass


class Queen(Pieces):
    def __init__(self, short_name, team, **kwargs):

        if team is Colors.WHITE:
            self.short_name = short_name if short_name not in Pieces.piece_names else str(Colors.WHITE.name) + 'Queen' + str(Queen.white_piece_index)
            Bishop.white_piece_index += 1

        elif team is Colors.BLACK:
            self.short_name = short_name if short_name not in Pieces.piece_names else str(Colors.BLACK.name) + 'Queen' + str(Queen.black_piece_index)
            Queen.black_piece_index += 1

        Pieces.piece_names.append(self.short_name)
        super().__init__(self.short_name, **kwargs)

    def move(self):
        pass


class King(Pieces):
    def __init__(self, short_name, team, **kwargs):

        if team is Colors.WHITE:
            self.short_name = short_name if short_name not in Pieces.piece_names else str(Colors.WHITE.name) + 'King' + str(King.white_piece_index)
            King.white_piece_index += 1

        elif team is Colors.BLACK:
            self.short_name = short_name if short_name not in Pieces.piece_names else str(Colors.BLACK.name) + 'King' + str(King.black_piece_index)
            King.black_piece_index += 1

        Pieces.piece_names.append(self.short_name)
        super().__init__(self.short_name, **kwargs)

    def move(self):
        pass