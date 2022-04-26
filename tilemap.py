from wave import Wave_write


level_map = [
    '                                                                                                                                      456                                                                          ',
    '                                                                                                                                      456                                                                          ',
    '                                                                                                                                      456                                                                          ',
    ' 13    123            13                                                                   123                                         452                                                                         ',
    ' 46 P                          E                                13                    E                 E                               452     E   E  E   E   E   E  E  E   E    E  E        13                 13',
    ' 4523         13              13                    E                                13                123                        122222555222222222222222222222222222222222222222222223                           ',
    ' 4556       13                                     13                    123                                                                                                                             1223      ',
    ' 46         46    13  13   E      E    E       12225523                       E     E                                                                                                         E 12223              ',
    '       2  1256    46  4522222222222222223    12555555552223  2       13      12223 12223     2   123   1223         E          123                                                       122222255556              ',
    '   E 126  455523  46  4556 45555555555556    45555555555556  43             155556 45555222226   45522255553   1222223        4555223   13                                                                         ',
    '12222556  455556  46  4555255555555555556    45555555555556  4523           455556 45555555556   45555555556   4555555223     4555556                                                                              ',
    '45555556  455556  46  4555555555555555556    45555555555556  4556           455556 45555555556   45555555556   4555555556     4555556                                                                              ',
]

tile_size = 64


class Resolution:
    def __init__(self, x=1280, y=720):
        self.x = x
        self.y = y

    def set_resolution_x(self, x):
        self.x = x

    def set_resolution_y(self, y):
        self.y = y

    def get_resolution_x(self):
        return self.x

    def get_resolution_y(self):
        return self.y


game_res = Resolution()
ww = game_res.get_resolution_x()
wh = game_res.get_resolution_y()
