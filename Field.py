from Settings import Settings

class Field:
    '''This class endcodes the field of playing'''
    def __init__(self, game):
        '''initialize the game field'''
        self.game = game # indicates the class Tetris()
        self.row = Settings.play_row
        self.column = Settings.play_column
        self.field = [[-1 for _ in range(self.column)]  
                      for _ in range(self.row)] # encode the 20*10 field as -1
        
    def edge_detection(self):
        '''This method determins if a block has hit an edge'''
        for x in range(0,16):
            if self.game.new_block.block()[self.game.new_block.rotation][x] == 1:
                i = int(x / 4)
                j = x % 4
                if self.game.new_block.x + j < 0 \
                or self.game.new_block.x + j > self.column - 1\
                or self.game.new_block.y + i - 2> self.row - 1\
                or (self.game.new_block.y-2+i > 0\
                and self.field[i+self.game.new_block.y-2]\
                [j+self.game.new_block.x] >= 0):
                    return True
        return False

    def stop(self):
        '''This methon indicates the block falls to the bottom and 
    stops, then assigns the value to field'''
        for x in range(0,16):
            if self.game.new_block.block()[self.game.new_block.rotation][x] == 1:
                i = int(x / 4)
                j = x % 4
                self.field[i+self.game.new_block.y-2][j+ self.game.new_block.x] =\
                self.game.new_block.color
        self.clear_row()
        self.game.generate_block()
        if self.edge_detection():
            self.game.lost()
        
    def clear_row(self):
        '''This method determines whether the entire row is filled, 
    and if so, clears the row'''
        line = 0
        for i in range(self.row):
            zero = 0
            for j in range(self.column):
                if self.field[i][j] == -1:
                    zero += 1
            if zero == 0:
                line += 1
                for x in range(i,1,-1):
                    for y in range(self.column):
                        self.field[x][y] = self.field[x-1][y]
                Settings.score += 500*line
                self.game.increase_block_speed()
                line = 0