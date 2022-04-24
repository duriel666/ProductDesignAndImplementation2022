from wave import Wave_write


level_map = [
    '                                                                                                                                       ',
    '                                                                                                                                       ',
    '                                                                                                                                       ',
    ' XX    XXX            XX                                                                   XXX                                         ',
    ' XX P                                                          XX                                                                      ',
    ' XXXX         XX              XX                                                    XX                XXX                              ',
    ' XXXX       XX     E                               XX                    XXX                                                           ',
    ' XX         XX    XX  XX                       XXXXXXXX                             E                                E                 ',
    '       X  XXXX    XX  XXXXXXXXXXXXXXXXXXX    XXXXXXXXXXXXXX  X               XXXXX XXXXX     X   XXX   XXXX    XXXXXXXXXX     XXXX     ',
    '     XXX  XXXXXX  XX  XXXX XXXXXXXXXXXXXX    XXXXXXXXXXXXXX  XX             XXXXXX XXXXXXXXXXX   XXXXXXXXXXX   XXXXXXXXXX     XXXXXXX  ',
    'XXXXXXXX  XXXXXX  XX  XXXXXXXXXXXXXXXXXXX    XXXXXXXXXXXXXX  XXXX           XXXXXX XXXXXXXXXXX   XXXXXXXXXXX   XXXXXXXXXX     XXXXXXX  '
]

tile_size = 64


class Resolution:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_resolution(self, x, y):
        self.x = x
        self.y = y

    def get_resolution_x(self):
        return self.x

    def get_resolution_y(self):
        return self.y


game_res = Resolution(1280, 720)
ww = game_res.get_resolution_x()
wh = game_res.get_resolution_y()
print(ww)
print(wh)
