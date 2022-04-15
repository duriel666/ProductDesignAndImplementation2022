import pygame


level_map = [
    '                                                                                                                                       ',
    '                                                                                                                                       ',
    '                                                                                                                                       ',
    ' XX    XXX            XX                                                                                                               ',
    ' XX P                                                          XX                                                                      ',
    ' XXXX         XX         XX                                                            XX                                              ',
    ' XXXX       XX     E                               XX                    XXX                                                           ',
    ' XX    X  XXXX    XX  XX                       XXXXXXXX                             E                                E                 ',
    '       X  XXXX    XX  XXXXXXXXXXXXXXXXXXX    XXXXXXXXXXXXXX  X               XXXXX XXXXX XXXX    XXX XXXX  X   XXXXXXXXXX     XXXXXX   ',
    '    XXXX  XXXXXX  XX  XXXX XXXXXXXXXXXXXX    XXXXXXXXXXXXXX  XX             XXXXXX XXXXXXXXXXX   XXXXXXXXXXX   XXXXXXXXXX     XXXXXXX  ',
    'XXXXXXXX  XXXXXX  XX  XXXXXXXXXXXXXXXXXXX    XXXXXXXXXXXXXX  XXXX           XXXXXX XXXXXXXXXXX   XXXXXXXXXXX   XXXXXXXXXX     XXXXXXX  '
]

tile_size = 64
screen_width = 1600
screen_height = len(level_map) * tile_size
