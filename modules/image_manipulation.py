from PIL import Image, ImageColor
import numpy as np

def replaceColor(image, target_color, replacement_color):
    target_color = ImageColor.getrgb(target_color)
    replacement_color = ImageColor.getrgb(replacement_color)

    image_arr = np.array(image)
    red, green, blue, alpha = image_arr.T

    replacement_areas = (red == target_color[0]) & (blue == target_color[1]) & (green == target_color[2])

    image_arr[..., :-1][replacement_areas.T] = replacement_color

    final_image = Image.fromarray(image_arr)

    return final_image

def loadPieceImages():
    PIECE_NAMES = (
        "king","queen","bishop","pawn","rook","knight"
    )
    piece_image_object= {"white": {}, "black": {}}

    #Load white pieces
    for piece in PIECE_NAMES:
        piece_img = Image.open("./resources/img/piece-set/white/{piece}.png".format(piece = piece))
        piece_image_object["white"][piece] = piece_img
    
    #Load black pieces
    for piece in PIECE_NAMES:
        piece_img = Image.open("./resources/img/piece-set/black/{piece}.png".format(piece = piece))
        piece_image_object["black"][piece] = piece_img

    return piece_image_object

def generateBoard(board, image_size, dark_square_color, light_square_color):
    piece_img_object = loadPieceImages()

    dark_squares_img = Image.open("./resources/img/dark_squares.png")
    light_squares_img = Image.open("./resources/img/light_squares.png")
    
    dark_squares_img = dark_squares_img.resize((image_size, image_size))
    light_squares_img = light_squares_img.resize((image_size, image_size))

    dark_squares_img = replaceColor(dark_squares_img, "#fff", dark_square_color)
    light_squares_img = replaceColor(light_squares_img, "#fff", light_square_color)

    full_board_img = Image.alpha_composite(dark_squares_img, light_squares_img)
    for y in range(0, len(board)):
        rank = board[len(board) - y - 1]
        for x, piece in enumerate(rank):
            if piece != None:
                full_board_img.alpha_composite(piece_img_object[piece.team][piece.name].resize((int(image_size/8 * 0.95), int(image_size/8 * 0.95))), dest = (int((image_size/8) * x), int(image_size/8 * y)))
    
    return full_board_img
