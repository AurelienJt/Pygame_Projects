import pygame

def text_pos(position,win,object):
    """
    This function returns relative positions for objects.

    - center: center x,y
    - x_center: center x
    - y_center: center y
    """
    if position == "center":
        return object.get_rect(center=win.get_rect().center)
    if position == "x_center":
        return object.get_rect(center=win.get_rect().center)[0]
    if position == "y_center":
        return object.get_rect(center=win.get_rect().center)[1]
    
def button_pos(postiton, win,button_width=None,button_height=None):
    """
    Creats relative position for buttons.

    - x_center_left: Center left x value
    - x_center_right: Center right x value
    """
    if postiton == "x_center_left":
        return (win.get_width()//3)-(button_width//2)
    
    elif postiton == "x_center_right":
        return (win.get_width()//3*2)-(button_width//2)
