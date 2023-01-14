class Settings:
    block_size = 30 # the size of block
    screen_width = 600 # the width of screen 
    screen_height =800 # the height of screen
    play_row = 20 # number of rows in the game interface
    play_column = 10 # number of columns in the game interface
    top_left_x = (screen_width - block_size * play_column) // 2 # the horizontal 
                        #coordinates in the top left corner of the game screen
    top_left_y = (screen_height - block_size * play_row) #vertical coordinates 
                                    #in the top left corner of the game screen
    fps = 120 # frame rate
    block_speed = 1 # block drop speed
    block_delay = 1000 / block_speed # block drop interval
    game_difficult = 1.1 # game difficulty
    score = 0 # score
    control_delay = 50 # key delay
     
