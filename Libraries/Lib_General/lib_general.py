import pygame

def text_pos(position,win,object):
    """
    This function returns relative positions for objects.
    """
    if position == "center":
        return object.get_rect(center=win.get_rect().center)
    if position == "x_center":
        return object.get_rect(center=win.get_rect().center)[0]
    if position == "y_center":
        return object.get_rect(center=win.get_rect().center)[1]