import pygame, sys, pymunk

def create_static_ball(space, pos):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body, 50)
    space.add(body, shape)
    return shape

def remove_static_ball(space, ball):
    space.remove(ball, ball.body)

def draw_static_balls(balls, screen):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pygame.draw.circle(screen, (0, 0, 0), (pos_x, pos_y), 50)
