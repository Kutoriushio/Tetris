import random
from Settings import Settings
class Block:
    '''Encode the seven Tetris blocks, each block has a color'''
    block1= [[0, 0, 0, 0,
              0, 0, 0, 0,
              0, 1, 1, 0,
              1, 1, 0, 0],
             [0, 0, 0, 0,
              1, 0, 0, 0,
              1, 1, 0, 0,
              0, 1, 0, 0]] # S type
    
    block2= [[0, 0, 0, 0,
              0, 0, 0, 0,
              1, 1, 0, 0,
              0, 1, 1, 0],
             [0, 0, 0, 0,
              0, 1, 0, 0,
              1, 1, 0, 0,
              1, 0, 0, 0]] # Z type
    
    block3 = [[0, 0, 0, 0,
               0, 0 ,0, 0,
               1, 0, 0, 0,
               1, 1, 1, 0],
              [0, 0, 0, 0,
               1, 1, 0, 0,
               1, 0, 0, 0,
               1, 0, 0, 0],
              [0, 0, 0, 0,
               0, 0, 0, 0,
               1, 1, 1, 0,
               0, 0, 1, 0],
              [0, 0, 0, 0,
               0, 1, 0, 0,
               0, 1, 0, 0,
               1, 1, 0, 0]] # J type
    
    block4= [[0, 0, 0, 0,
               0, 0 ,0, 0,
               0, 0, 1, 0,
               1, 1, 1, 0],
              [0, 0, 0, 0,
               1, 0, 0, 0,
               1, 0, 0, 0,
               1, 1, 0, 0],
              [0, 0, 0, 0,
               0, 0, 0, 0,
               1, 1, 1, 0,
               1, 0, 0, 0],
              [0, 0, 0, 0,
               1, 1, 0, 0,
               0, 1, 0, 0,
               0, 1, 0, 0]] # L type
    
    block5 = [[0, 0, 0, 0,
               0, 0 ,0, 0,
               0, 1, 0, 0,
               1, 1, 1, 0],
              [0, 0, 0, 0,
               1, 0, 0, 0,
               1, 1, 0, 0,
               1, 0, 0, 0],
              [0, 0, 0, 0,
               0, 0, 0, 0,
               1, 1, 1, 0,
               0, 1, 0, 0],
              [0, 0, 0, 0,
               0, 1, 0, 0,
               1, 1, 0, 0,
               0, 1, 0, 0]] # T type
    
    block6 = [[0, 0, 0, 0,
               0, 0, 0, 0,
               1, 1, 0, 0,
               1, 1, 0, 0]] # O type
    
    block7 = [[0, 0, 0, 0,
               0, 0 ,0, 0,
               0, 0, 0, 0,
               1, 1, 1, 1],
              [0, 1, 0, 0,
               0, 1, 0, 0,
               0, 1, 0, 0,
               0, 1, 0, 0]] # I type
    
    blocks = [block1, block2, block3, block4, block5, block6, block7]
    colors = [[0, 255, 0],
              [255, 0, 0],
              [0, 0, 255],
              [255, 127, 0],
              [128, 0, 128],
              [255, 255, 0],
              [0, 255, 255]] # color of blocks
    
    def __init__(self, game, x, y):
        '''initialize blocks'''
        self.game = game
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.blocks)-1)
        self.color = self.type
        self.rotation = 0
    
    def block(self):
        '''This method return the block of specific type and color'''
        return self.blocks[self.type]
    
    def move(self):
        '''This method means that the block moves down every second'''
        if self.game.now > self.game.block_time2move:
            self.game.block_time2move = self.game.now + Settings.block_delay
            self.go_down()
    
    def rotate(self):
        '''This method means that the shape of the block after rotation'''
        self.rotation = (self.rotation+1) %\
        (len(self.blocks[self.type]))
        if self.game.field.edge_detection():
            self.rotation -= (self.rotation+1) %\
            (len(self.blocks[self.type]))
            
    def go_left_right(self,dx):
        '''This method indicates that the square moves one grid 
    to the left or the right'''
        self.x += dx
        if self.game.field.edge_detection():
            self.x -= dx
    
    def go_down(self):
        '''This methon indicates that the block falls one grid'''
        self.y += 1
        if self.game.field.edge_detection():
            self.y -= 1
            self.game.field.stop()
    
    def go_bottom(self):
        '''This methon indicates that the block falls straight to the 
    bottom'''
        while not self.game.field.edge_detection():
            self.y += 1
        self.y -= 1
        self.game.field.stop()