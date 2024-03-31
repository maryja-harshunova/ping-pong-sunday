from pygame import *

class GameSprite(sprit.Sprite):
    def __init__ (self, image, x, y, width, height, speed, speed_x = 0, speed_y = 0):
        super().__init__()
        self.img = transform.scale(image.load(image), (width, height))
        self.speed = speed
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))