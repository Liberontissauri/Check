class Piece:
    def __init__(self, name, team):
        self.name = name
        self.team = team

def convertFENCharacterToPiece(character):
    piece_translation_dictionary = {
        "p": lambda: Piece("pawn", "black"),
        "P": lambda: Piece("pawn", "white"),
        "n": lambda: Piece("knight", "black"),
        "N": lambda: Piece("knight", "white"),
        "b": lambda: Piece("bishop", "black"),
        "B": lambda: Piece("bishop", "white"),
        "r": lambda: Piece("rook", "black"),
        "R": lambda: Piece("rook", "white"),
        "q": lambda: Piece("queen", "black"),
        "Q": lambda: Piece("queen", "white"),
        "k": lambda: Piece("king", "black"),
        "K": lambda: Piece("king", "bwhite"),
    }
    translated_piece = piece_translation_dictionary.get(character)
    if translated_piece is None:
        raise ValueError("Tried passing a value not included in the FEN standard")
    return piece_translation_dictionary[character]()


