import pygame

import random
#Set up game window
pygame.init()
window_width = 400
window_height = 600
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Flappy Bird")

#Load game assets
bird_width = 50
bird_height = 40
bird_image = pygame.image.load("bird.png").convert_alpha()
bird_image = pygame.transform.scale(bird_image, (bird_width, bird_height))
pipe_width = 70
pipe_height = 400
pipe_image = pygame.image.load("pipe.png").convert_alpha()
pipe_image = pygame.transform.scale(pipe_image, (pipe_width, pipe_height))

#set up game variables
bird_x = 50
bird_y = 200
bird_velocity = 0
gravity = 0.3
jump_strength = 6
pipe_gap = 150
pipe_frequency = 100
pipes = []

#set up game functions
def draw_bird():
  game_window.blit(bird_image, (bird_x, bird_y))

def update_bird():
  global bird_y, bird_velocity
  bird_velocity += gravity
  bird_y += bird_velocity

def jump():
  global bird_velocity
  bird_velocity = -jump_strength

def draw_pipe(pipe):
  top_pipe_height = pipe[0]
  bottom_pipe_height = pipe[1]
  pipe_x = pipe[2]
  game_window.blit(pipe_image, (pipe_x, 0), (0, 0, pipe_width, top_pipe_height))
  game_window.blit(pipe_image, (pipe_x, window_height - bottom_pipe_height), (0, pipe_height - bottom_pipe_height, pipe_width, bottom_pipe_height))

def update_pipes():
  global pipes
  for pipe in pipes():
    pipe[2] -= 2
  if len(pipes) > 0 and pipes [0][2] < -pipe_width:
    pipes.pop(0)
  if len(pipes) ==0 or pipes [-1][2] < window_height - pipe_frequency:
    top_pipe_height = random.randit(100, window_height - pipe_gap - 100)
    bottom_pipe_height = window_height - pipe_gap - top_pipe_height
    pipes.append([top_pipe_height, bottom_pipe_height, window_width])

def check_collisions():
  if bird_y < 0 or bird_y + bird_height > window_height:
    return True
  for pipe in pipes:
    if bird_x + bird_width > pipe[2] and bird_x < pipe[2] + pipe_width:
      if bird_y < pipe[0] or bird_y + bird_height > window_height - pipe[1]:
        return True
  return False

# Game loop
clock = pygame.time.Clock()
game_over = False
while not game_over:
  clock.tick(60)

  for even in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
    if event.type == pygame.KeyDown:
      if event.key == pygame.k_space:
        jump()
  game_window.fill((255, 255, 255))
  update.bird()
  draw_bird()
  update_pipes()
  for pipe in pipes:
    draw_pipe(pipe)
  if check_collisions():
    game_over = True
  pygame.display.update()

pygame.quit()
