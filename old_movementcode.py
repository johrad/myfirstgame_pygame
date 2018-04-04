print("All is commenets")

# class Player():
#     def __init__(self):
#         global jumping
#         self.x_pos = 250
#         self.y_pos = 250
#         self.npc_color = (255, 0, 255)
#         self.npc_width = 15
#         self.npc_height = 15
#         self.npc_vel = 5
#         self.jumping_height = 10
#         self.jumping = False
#         self.standing = True
#
#
#
#
#
# if key[pygame.K_SPACE]:
#         man.jumping = True
#
#         if man.jumping_height == 10:
#             jumping_sound_1.play()
#     if not(man.jumping):
#         if (key[pygame.K_w] or key[pygame.K_UP]) and (man.y_pos > man.npc_vel):
#             man.y_pos -= man.npc_vel
#         if (key[pygame.K_s] or key[pygame.K_DOWN]) and (man.y_pos <
#                                                         (height - man.npc_height - man.npc_vel)):
#             man.y_pos += man.npc_vel
#     else:
#         if man.jumping_height >= -10:
#             magic_jump_num = 1
#
#             if man.jumping_height < 0:
#                 magic_jump_num = -1
#
#             man.y_pos -= (man.jumping_height ** 2) * 0.2 * magic_jump_num
#             man.jumping_height -= 1
#             # "magic_jump_num" turns the character around when jumping
#         else:
#             man.jumping = False
#             man.jumping_height = 10
#
#     if (key[pygame.K_d] or key[pygame.K_RIGHT]) and (man.x_pos <
#                                                      (width - man.npc_vel - man.npc_vel)):
#         man.x_pos += man.npc_vel
#
#     if (key[pygame.K_a] or key[pygame.K_LEFT]) and (man.x_pos > man.npc_vel):
#         man.x_pos -= man.npc_vel
#
#     if key[pygame.K_ESCAPE] or (key[pygame.K_e] and (key[pygame.K_LCTRL] or key[pygame.K_RSHIFT])):
#         running = False
