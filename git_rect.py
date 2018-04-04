import pygame
version = "0.00.3"
pygame.init()
pygame.font.init()
pygame.mixer.init()
clock = pygame.time.Clock()

FPS = 60
VOL = 0.2


if pygame.init() == (6, 0):
    print("Pygame successfully initalized ")
    print("Video driver: {}".format(pygame.display.get_driver()))
else:
    print("Oh shit, something is wrong\nError code: 00000000Ex1")


class Drawdisplay():
    def __init__(self):
        global width
        global height
        width = 500
        height = 500
        global fill_color
        fill_color = (0, 0, 0)
        self.my_font = pygame.font.SysFont('Arial', 17)

    def draw_window(self):
        global display
        display = pygame.display.set_mode((width, height))
        display.fill(fill_color)
        pygame.display.flip()

    def draw_text(self):
        text_surface = self.my_font.render(("Version {}".format(version)),
                                           False,
                                           ((255, 30, 50)))
        display.blit(text_surface, (0, 0))
        pygame.display.flip()


class Player():
    def __init__(self):
        global jumping
        self.x_pos = 250
        self.y_pos = 250
        self.npc_color = (200, 200, 200)
        self.npc_width = 20
        self.npc_height = 20
        self.npc_vel = 5
        self.jumping_height = 10
        self.jumping = False
        self.standing = True

    def movement(self):
        pass

    def npc_draw(self):
        pygame.draw.rect(display, self.npc_color, (self.x_pos,
                                                   self.y_pos, self.npc_width,
                                                   self.npc_height))
        pygame.display.flip()


def mixer_start(vol):
    mixer_volume = vol
    global jumping_sound_1
    jumping_sound_1 = pygame.mixer.Sound('jump.ogg')
    pygame.mixer.music.load('Backround_intense.ogg')
    pygame.mixer.music.set_volume(mixer_volume)

    pygame.mixer.music.play(-1, 0.0)


game_window = Drawdisplay()
man = Player()

mixer_start(VOL)

game_window.draw_window()
game_window.draw_text()
man.npc_draw()
running = True
while running:
    clock.tick(FPS)
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if key[pygame.K_SPACE]:
        man.jumping = True

        if man.jumping_height == 10:
            jumping_sound_1.play()
    if not(man.jumping):
        if (key[pygame.K_w] or key[pygame.K_UP]) and (man.y_pos > man.npc_vel):
            man.y_pos -= man.npc_vel
        if (key[pygame.K_s] or key[pygame.K_DOWN]) and (man.y_pos <
                                                        (height - man.npc_height - man.npc_vel)):
            man.y_pos += man.npc_vel
    else:
        if man.jumping_height >= -10:
            magic_jump_num = 1

            if man.jumping_height < 0:
                magic_jump_num = -1

            man.y_pos -= (man.jumping_height ** 2) * 0.2 * magic_jump_num
            man.jumping_height -= 1
            # "magic_jump_num" turns the character around when jumping
        else:
            man.jumping = False
            man.jumping_height = 10

    if (key[pygame.K_d] or key[pygame.K_RIGHT]) and (man.x_pos <
                                                     (width - man.npc_vel - man.npc_vel)):
        man.x_pos += man.npc_vel

    if (key[pygame.K_a] or key[pygame.K_LEFT]) and (man.x_pos > man.npc_vel):
        man.x_pos -= man.npc_vel

    if key[pygame.K_ESCAPE] or (key[pygame.K_e] and (key[pygame.K_LCTRL] or key[pygame.K_RSHIFT])):
        running = False

    game_window.draw_window()
    man.npc_draw()
    game_window.draw_text()


pygame.quit()
print("Thank you for playing!")
