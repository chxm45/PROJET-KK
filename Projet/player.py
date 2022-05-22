import pygame



class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('images/girl sheet.png')
        self.image = self.get_image(48, 0)
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.images = {
            'down': self.get_image(0,0),
            'left': self.get_image(0, 48),
            'right': self.get_image(0, 96),
            'up': self.get_image(0, 144)
        }
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()
        self.speed = 2.7


    def get_image(self, x, y):
        image = pygame.Surface([48, 48], pygame.SRCALPHA)
        image.blit(self.sprite_sheet, (0, 0), (x, y, 48, 48))
        return image



    def save_location(self): self.old_position = self.position.copy()

    def change_animation(self, name): self.image = self.images[name]

    def move_right(self): self.position[0] += self.speed

    def move_left(self): self.position[0] -= self.speed

    def move_up(self): self.position[1] -= self.speed

    def move_down(self): self.position[1] += self.speed


    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom