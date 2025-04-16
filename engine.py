import pygame, sys, pymunk
import apple, static_ball
import main

#HELLO THIS IS TEST LINE

def engine():
        

    screen = pygame.display.set_mode((1280, 720)) #create display surface
    clock = pygame.time.Clock() #create game clock
    space = pymunk.Space()
    space.gravity = (10, 100) #0 horizontal, 500 vertical gravity
    apples = []
    apple_surface = pygame.image.load('assets/apple_red.png')

    balls = []


    click_sound = pygame.mixer.Sound("assets/iamsteve.mp3")



    while True: #Game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main.main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_sound.play()
                apples.append(apple.create_apple(space, event.pos))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mouse_pos = pygame.mouse.get_pos()
                    balls.append(static_ball.create_static_ball(space, mouse_pos))
                if event.key == pygame.K_c:
                    for ball in balls:
                        static_ball.remove_static_ball(space, ball)
                    balls.clear()


        
        screen.fill((217, 217, 217)) #bg colour
        apple.draw_apples(apples, screen, apple_surface)
        static_ball.draw_static_balls(balls, screen)
        space.step(1/50)
        pygame.display.update() #render frame
        clock.tick(120) #limit fps to 120
