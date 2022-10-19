import sys
import pygame
import random
import time
#there are many of the locations in my computer as the assets please change that to your 2-D assets location
pygame.init()
y=0
car_x_movement = 0
car_left = +200
car_right = -200
fps = 300
#random_image = ["images-removebg-preview.png"]
random_image = ["car_game_obstacle_new__new_1.png"]
random_org = random.choice(random_image)
obstacle_img = pygame.image.load(random_org)
obstacle_list = []
spawn_obstacle = pygame.USEREVENT
pygame.time.set_timer(spawn_obstacle,1200)
game_active = True
def create_obstacle():
    random_width = random.choice(random_obstacle_list)
    obstacle = obstacle_img.get_rect(center = (random_width,10))
    #obstacle_right = obstacle_img.get_rect(center = (400,300))
    return obstacle
    #return obstacle_right
def move_obstacle(obstacles):
    for obstacle in obstacles:
        obstacle.centery=obstacle.centery+2
    return obstacles
def draw_obstacle(obstacles):
    for obstacle in obstacles:
        screen.blit(obstacle_img,obstacle)
def collision(pipes):
    for pipe in pipes:
        if car_rect.colliderect(pipe):
            return False
    return True
def road_moving():
    screen.blit(road,(0,y))
    screen.blit(road,(0,y-500))
    screen.blit(road,(0,y))
    screen.blit(road,(0,y-500))
def game_over():
    game_over_image = pygame.image.load("image_2022-05-22_192311607.png")
    game_over_rect = game_over_image.get_rect(center = (300,250))
    screen.blit(game_over_image,game_over_rect)
random_obstacle_list = [200,400,350]
intro = pygame.image.load("game_intro.png")
screen = pygame.display.set_mode((600,500))
road = pygame.image.load("C:/Users/hp/Pictures/kali linux/python application demo/cartoon_road.png")
car = pygame.image.load("C:/Users/hp/Pictures/kali linux/python application demo/car_game_.png")
car_rect = car.get_rect(center=(230,400))
clock = pygame.time.Clock()
pygame.display.set_caption("Crazy Car Riding.....")
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                car_x_movement = car_x_movement+car_left
            if event.key==pygame.K_RIGHT:
                car_x_movement = car_x_movement+car_right
        if event.type==spawn_obstacle:
            obstacle_list.append(create_obstacle())
            #print(obstacle_list)
    #pygame.time.delay(6000)         
    if game_active:
        y+=1
        road_moving()
        if y>=500:
            y=0
        obstacle_list = move_obstacle(obstacle_list)
        car_rect.centerx = car_rect.centerx-car_x_movement
        screen.blit(car,car_rect)
        if car_x_movement>=-32 or car_x_movement<=32:
            car_x_movement=0
        if car_rect.centerx<=200:
            car_x_movement=-8
        if car_rect.centerx>=400:
            car_x_movement=8
        draw_obstacle(obstacle_list)
        game_active = collision(obstacle_list)
    #screen.blit(intro,(300,250))
    else:
        while True:
            game_over()
            game_over()
            game_over()
            continue
        sys.exit()
    pygame.display.update()
    clock.tick(fps)
    #print("now fps is: "+ str(fps))
