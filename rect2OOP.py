import pygame
import os
version = "0.00.3"
pygame.init()
pygame.font.init()
pygame.mixer.init(44100, 16, 2, 4096)
clock = pygame.time.Clock()

# set up asset folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
print("Im in path: {}".format(img_folder))


class Drawdisplay():
    def __init__(self):
        global width
        global height
        width = 500
        height = 500
        global fill_color
        fill_color = (255, 255, 0)
        self.my_font = pygame.font.SysFont('Arial Black', 17)

    def window_init(self):
        global display
        display = pygame.display.set_mode((width, height))

    def draw_window(self):
        display.fill(fill_color)
        pygame.display.flip()

    def draw_text(self):
        text_surface = self.my_font.render(("Version " + version),
                                           False,
                                           ((0, 0, 0)))
        display.blit(text_surface, (0, 0))
        pygame.display.flip()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder,
                                                    'p1_stand.png')).convert()
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)


def mixer_start(vol):
    mixer_volume = vol
    global jumping_sound_1

    jumping_sound_1 = pygame.mixer.Sound('jump.ogg')
    pygame.mixer.music.load('Backround_intense.ogg')
    pygame.mixer.music.set_volume(mixer_volume)

    pygame.mixer.music.play(-1, 0.0)


game_window = Drawdisplay()
player = Player()

# mixer_start(0.35)

all_sprites = pygame.sprite.Group(player)
game_window.window_init()
game_window.draw_window()
game_window.draw_text()

running = True
while running:
    clock.tick(30)
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if key[pygame.K_ESCAPE]:
        running = False

    # Update
    all_sprites.update()

    # Drawing stuff
    game_window.draw_window
    all_sprites.draw(display)
    game_window.draw_text()


pygame.quit()
print("Thank you for playing!\n(C) Johan-Petter R. Dragic")
