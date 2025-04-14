import pygame, sys, pymunk


def create_apple(space, pos):
    body = pymunk.Body(1, 100, body_type = pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, 80)
    space.add(body, shape)
    return shape

def draw_apples(apples, screen, apple_surface):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)
        apple_rect = apple_surface.get_rect(center = (pos_x, pos_y))
        screen.blit(apple_surface, apple_rect)
        



