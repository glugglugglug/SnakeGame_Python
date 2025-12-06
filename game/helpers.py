import pyxel



#helper func for calc start x value for centred text
def center_text(text, page_width, char_width = pyxel.FONT_WIDTH):
    text_width = len(text) * char_width
    return (page_width - text_width) / 2


#helper func for calc start x value for right aligned text
def right_text(text, page_width, char_width = pyxel.FONT_WIDTH):
    text_width = len(text) * char_width
    return page_width - (text_width + char_width) 