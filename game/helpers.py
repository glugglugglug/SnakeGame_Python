import pyxel



#helper func for calc start x value for centred text
def center_text(text, page_width, char_width = pyxel.FONT_WIDTH):
    text_width = len(text) * char_width
    return (page_width - text_width) / 2

#helper to vertically centre a text (y value)
def arrange_text_y(text, page_height, divisor, char_height = pyxel.FONT_HEIGHT):
    return (page_height - char_height) / divisor

#helper func for calc start x value for right aligned text
def right_text(text, page_width, char_width = pyxel.FONT_WIDTH):
    text_width = len(text) * char_width
    return page_width - (text_width + char_width) 