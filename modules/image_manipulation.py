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

