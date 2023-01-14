import pygame
from Block import Block
from Settings import Settings
from Field import Field
from Draw import Draw

class Tetris:
    '''This is the main class of the game'''
    def __init__(self):
        '''Initialise the time of the game 
    and call the other classes to create objects'''
        pygame.init()
        pygame.display.set_caption('Tetris')
        self.window = pygame.display.set_mode((Settings.screen_width, 
                                          Settings.screen_height))
        self.clock = pygame.time.Clock()
        self.block_time2move = pygame.time.get_ticks() + Settings.block_delay
        self.control_delay = pygame.time.get_ticks() + Settings.control_delay
        self.flag = True # determine the status of game
        self.now = 0
        self.new_block = Block(self, 3, 0)
        self.next_block = Block(self, 3, 0)
        self.field = Field(self)
        self.draw = Draw(self)
        self.myfont = pygame.font.SysFont("Tetris", 100)
        self.game_difficult = Settings.game_difficult
        self.game_state = 1
        
    def main_menu(self):
        '''Game's main menu'''
        menu = True
        while menu:
            self.window.fill((255,255,255))
            self.draw.text_to_screen('Main Menu', (0,0,0), 
                                Settings.screen_width / 2 - 180, 
                                Settings.screen_height / 2 - 50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        menu = False
                        Tetris().run()
            pygame.display.flip()
                    
    def run(self):
        '''The main loop of the game'''
        '''Calling other methods'''
        while self.flag:
            self.keys = pygame.key.get_pressed()
            self.now = pygame.time.get_ticks()
            self.process_event()
            self.draw.draw_screen()
            self.draw.draw_gird()
            self.new_block.move()
            self.draw.draw_block()
            self.draw.draw_score()
            pygame.display.flip()
            self.clock.tick(Settings.fps)


        
    def process_event(self):
        '''Handling user keyboard input messages'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.flag = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.new_block.go_bottom()
                if event.key == pygame.K_r:
                    self.restart()
                if event.key == pygame.K_UP:
                    self.new_block.rotate()
                if event.key == pygame.K_p:
                    self.pause()             
        if self.now > self.control_delay:
            self.control_delay = pygame.time.get_ticks() +\
            Settings.control_delay
            if self.keys[pygame.K_LEFT]:
                self.new_block.go_left_right(-1)
            if self.keys[pygame.K_RIGHT]:
                self.new_block.go_left_right(1)
            if self.keys[pygame.K_DOWN]:
                self.new_block.go_down()
                
    def generate_block(self):
        '''Generate new blocks'''
        self.new_block = self.next_block
        self.next_block = Block(self, 3, 0)
    
    
    def increase_block_speed(self):
        '''Increases the fall speed of blocks as the score increases'''
        if Settings.score % 1000 == 0:
            Settings.block_speed *= Settings.game_difficult
            Settings.block_delay = 500 / Settings.block_speed
    
    def pause(self):
        '''Pause the game'''
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False
            self.window.fill((255,255,255))
            self.draw.text_to_screen('Game Paused', (127,127,127), 
                                Settings.screen_width / 2 - 220, 
                                Settings.screen_height / 2 - 100)
            
            pygame.display.flip()
                
    def lost(self):
        '''Determining if the upper bound is exceeded'''
        '''if it is, the game is over'''
        lost = True
        while lost:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        lost = False
                        self.restart()
            self.window.fill((255,255,255))
            self.draw.text_to_screen('You Lost', (0,0,0), 
                                Settings.screen_width / 2 - 150, 
                                Settings.screen_height / 2 - 50)
            pygame.display.flip()
    
    def restart(self):
        '''Restart the game'''
        Settings.block_speed = 1
        Settings.block_delay = 1000 / Settings.block_speed
        Settings.score = 0
        Tetris().run()
        
if __name__ == '__main__':
    Tetris().main_menu()
