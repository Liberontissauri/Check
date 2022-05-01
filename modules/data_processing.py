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


def convertFenRankToArray(FEN_rank_string):
    rank_array = []
    for character in FEN_rank_string:
        
        if character.isnumeric():
            integer_of_character = int(character)
            for _ in range(0, integer_of_character):
                rank_array.append(None)
            
            continue
        
        rank_array.append(convertFENCharacterToPiece(character))
    
    if len(rank_array) > 8:
        raise RuntimeError("Maximum piece limit exceeded", "limit_exceeded")
    elif len(rank_array) < 8:
        raise RuntimeError("Non-full board", "non_full_board")
    
    return rank_array

def divideFENIntoRankStrings(FEN_string):
    divided_ranks = ""
    if FEN_string.find(" ") != -1:
        divided_ranks = FEN_string[:FEN_string.find(" ")].split("/")
    else:
        divided_ranks = FEN_string.split("/")
    
    if len(divided_ranks) > 8:
        raise RuntimeError("Rank limit exceeded", "limit_exceeded")
    return divided_ranks

