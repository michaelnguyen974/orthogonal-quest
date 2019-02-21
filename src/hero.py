import pygame as pg

from src.constants import WIDTH, HEIGHT, TILESIZE, GREEN

class Hero(pg.sprite.Sprite):
    def __init__(self, game, x_pos, y_pos):

        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x_pos
        self.y = y_pos

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy
    
    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls_sprites:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                print("Wall collision")
                return True
        return False

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE