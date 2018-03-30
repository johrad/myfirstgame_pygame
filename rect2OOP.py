import pygame
version = "0.00.3"
pygame.init()
pygame.font.init()
pygame.mixer.init()
clock = pygame.time.Clock()

print(pygame.init())
print("Video driver:{}".format(pygame.display.get_driver()))


class Drawdisplay:
    def __init__(self):
        global width
        global height
        width = 500
        height = 500
        global fill_color
        fill_color = (255, 255, 0)
        self.my_font = pygame.font.SysFont('Arial Black', 17)

    def draw_window(self):
        global display
        display = pygame.display.set_mode((width, height))
        display.fill(fill_color)
        pygame.display.flip()

    def draw_text(self):
        text_surface = self.my_font.render(("Version " + version), False, ((0, 0, 0)))
        display.blit(text_surface, (width/1.2, height/2))
        pygame.display.flip()


class Player():
    def __init__(self):
        self.x_pos = 250
        self.y_pos = 250
        self.npc_color = (255, 0, 255)
        self.npc_width = 15
        self.npc_height = 15
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


game_window = Drawdisplay()
man = Player()

game_window.draw_window()
game_window.draw_text()
man.npc_draw()
running = True
while running:
    clock.tick(60)
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            pass

    if not(man.jumping):
        if key[pygame.K_w] and man.y_pos > man.npc_vel:
            man.y_pos -= man.npc_vel

    if key[pygame.K_ESCAPE] or (key[pygame.K_e] and (key[pygame.K_LCTRL] or key[pygame.K_RSHIFT])):
        running = False

    game_window.draw_window()
    man.npc_draw()
    game_window.draw_text()


pygame.quit()
print("Thank you for playing!")
