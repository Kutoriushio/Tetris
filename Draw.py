import pygame
from Settings import Settings
class Draw:
    '''This class implements game visualisation'''
    def __init__(self, game):
        self.game = game # indicates the class Tetris()
        
    def draw_score(self):
        '''This method draws score of game'''
        self.text_to_screen("Score {}".format(Settings.score), 
                            (127,127,127), 5, 10)
    
    def draw_gird(self):
        '''This method draws grids of game'''
        for i in range(Settings.play_row):
            for j in range(Settings.play_column):
                pygame.draw.rect(self.game.window, (255, 255, 255), 
                (Settings.top_left_x+j*Settings.block_size,
        Settings.top_left_y+i*Settings.block_size, Settings.block_size,
                                        Settings.block_size), 1)
                if self.game.field.field[i][j] >= 0:
                    pygame.draw.rect(self.game.window,
                    (self.game.new_block.colors[self.game.field.field[i][j]]),
                    (Settings.top_left_x+j*Settings.block_size+1,
                     Settings.top_left_y+i*Settings.block_size+1,
                     Settings.block_size-3,Settings.block_size-3))
        
        for i in range(5):
            for j in range(5):
                pygame.draw.rect(self.game.window, (255,255,255), 
                                 (Settings.block_size*14+j*Settings.block_size,
                        Settings.block_size+i*Settings.block_size,Settings.block_size,
                        Settings.block_size), 1)
    
    def draw_block(self):
        '''This methond draws different blocks'''
        for x in range(0,16):
            if self.game.new_block.block()[self.game.new_block.rotation][x] == 1:
                i = int(x / 4)
                j = x % 4
                pygame.draw.rect(self.game.window, 
                                 self.game.new_block.colors[self.game.new_block.color],
                     (Settings.top_left_x+(j+self.game.new_block.x)*Settings.block_size+1, 
                      Settings.top_left_y+(i+self.game.new_block.y-2)*Settings.block_size+1,
                     Settings.block_size-3, Settings.block_size-3))
                
        for x in range(0,16):
            if self.game.next_block.block()[self.game.next_block.rotation][x] == 1:
                i = int(x / 4)
                j = x % 4
                pygame.draw.rect(self.game.window, 
                                 self.game.next_block.colors[self.game.next_block.color],
                     (12*Settings.block_size+(j+self.game.next_block.x)*Settings.block_size+1, 
                      Settings.block_size+(i+self.game.next_block.y-1)*Settings.block_size+1,
                     Settings.block_size-3, Settings.block_size-3))
                
    def draw_screen(self):
        '''This method draws game interface'''
        self.game.window.fill((0, 0, 0))
        pygame.draw.rect(self.game.window, (128, 128, 128), (Settings.top_left_x,
                                                   Settings.top_left_y, 
                                    Settings.block_size*Settings.play_column, 
                                    Settings.block_size*Settings.play_row))
        
        pygame.draw.rect(self.game.window, (128,128,128), (Settings.block_size*14,Settings.block_size,
                                    Settings.block_size*5,Settings.block_size*5))
        
    def text_to_screen(self, msg, color, x, y):
        '''This method draws the text on the game interface'''
        # msg: text to be drawed
        # color: the color of text
        # x, y: the coordinates of the text
        text = self.game.myfont.render(msg, 1, color)
        self.game.window.blit(text, (x, y))