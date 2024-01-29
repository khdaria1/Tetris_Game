import pygame

class Grid:
    def __init__(self):     
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = self.get_cell_colors()
        
    def print_grid(self):    
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()
    
    def get_cell_colors(self):  
        dark_grey = (26,31,40)
        green = (47,230,23)
        red = (232,18,18)
        orange = (226,116,17)
        yellow = (237,234,4)
        purple = (166,0,247)
        cyan = (21,204,209)
        blue = (13,64,216)
        
        return [dark_grey, green, red, orange, yellow, purple, cyan, blue]
    
    def draw(self, screen):
        gapOutboxWithInbox = 2
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(
                    (self.cell_size * column) + gapOutboxWithInbox,    # box start point : x 
                    (self.cell_size * row) + gapOutboxWithInbox,       # box start point : y
                    (self.cell_size) - gapOutboxWithInbox,             # box width
                    (self.cell_size) - gapOutboxWithInbox              # box height
                )
                pygame.draw.rect(
                    screen,
                    color=self.colors[cell_value],
                    rect=cell_rect
                )