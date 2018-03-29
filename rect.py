import pygame
pygame.init()


def check_for_error():
    if pygame.init() == (6, 0):
        print("Pygame has been successfully initialized ")
    else:
        print("this is not supposed ot happen wtf\n check for errors")
        print(pygame.init())
    Video_driver = pygame.display.get_driver()
    print(Video_driver)


check_for_error()


class Settings():
    def __init__(self):
        self.black = (000, 000, 000)
        self.white = (255, 255, 255)
        self.red = (255, 000, 000)
        self.green = (000, 255, 000)
        self.blue = (000, 000, 255)

    def display_settings(self):
        self.width = 500
        self.height = 500
        self.caption = "This is a cool window"
        self.version = "0.00.2"
        self.Fill_color = black
        # self.m_volume = 0.3

    def drawdisplay(self):
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        screen.fill(Fill_color)

        # Set version text
        my_font = pygame.font.SysFont('Arial', 15)
        text_surface = my_font.render(("Version " + version), False, (blue))
        screen.blit(text_surface, (0, 0))


class Player():
    def __init__(self):
        self.x_pos = 250
        self.y_pos = 250
        self.npc_color = (255, 0, 0)
        self.npc_width = 15
        self.npc_height = 15
        self.npc_vel = 5
        self.jumping_height = 10

    def movement(self, key):

        if key[pygame.K_LEFT] and x_pos > npc_vel:
            x_pos -= npc_vel

        if key[pygame.K_RIGHT] and x_pos < width - npc_vel - npc_width:
            x_pos += npc_vel

        if key[pygame.K_SPACE]:
            if jumping_height == 10:
                jumping_sound.play()
            jumping = True

        if not(jumping):
            if key[pygame.K_UP] and y_pos > npc_vel:
                y_pos -= npc_vel

            elif key[pygame.K_DOWN] and y_pos < height - npc_height - npc_vel:
                y_pos += npc_vel

        else:
            if jumping_height >= -10:
                neg_num = 1

                if jumping_height < 0:
                    neg_num = -1
                y_pos -= (jumping_height ** 2) * 0.2 * neg_num
                jumping_height -= 1

            else:
                jumping = False
                jumping_height = 10


# Makes window and gets display caption



# Display text
pygame.font.init()


# Flips display
pygame.display.flip()


# loading up sounds
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)

jumping_sound = pygame.mixer.Sound('jump.ogg')
background_music = pygame.mixer.music.load('Backround_intense.ogg')
pygame.mixer.music.set_volume(m_volume)

pygame.mixer.music.play(-1, 0.0)  # Starts background music

# Setting "rectangle" details


# States of npc
jumping = False
standing = True

'''
        if key_hold[pygame.K_ESCAPE]:
           my_Qfont = pygame.font.SysFont('Arial Black', 20)
           my_Qfont2 = pygame.font.SysFont('Arial', 13)

           text_quiting = my_Qfont.render(("QUITING..."), False, (blue))
           #screen.blit(text_quiting, (250,0))

           text_quiting2 = my_Qfont2.render(("Keep holding ESC"), False, (blue))
           screen.blit(text_quiting2, (250,20))
'''

running = True
###############################################################
# Starting game loop
while running:
    pygame.time.delay(35)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()

    screen.fill(Fill_color)
    pygame.draw.rect(screen, npc_color, (x_pos, y_pos, npc_width, npc_height))
    pygame.display.update()
    pygame.font.init()

    my_font = pygame.font.SysFont('Arial', 17)
    text_surface = my_font.render(("Version " + version), False, (white))
    screen.blit(text_surface, (0, 0))
    pygame.display.flip()

    if key[pygame.K_ESCAPE]:
        running = False


print("Thank you for playing the game\n(C) Johan-Petter R. Dragic")
pygame.quit()
