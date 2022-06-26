import this
from tkinter import TRUE
import pygame
from sys import exit

def add_zero_front(value):
    if value < 10:
        return "0" + str(value)
    else:
        return str(value)
    

pygame.init()
pause = True
second = 0
minute = 0
hour = 0
day = 0
timer_data = str(day) + ":" + add_zero_front(hour) + ":" + add_zero_front(minute) + ":" + add_zero_front(second)
clock = pygame.time.Clock()

time_delay = 1000 # 1 seconds
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event , time_delay )



screen = pygame.display.set_mode((400,150))
pygame.display.set_caption("Timer")
timer_font = pygame.font.Font("Font/Roboto-Light.ttf",75)
timer_surface = timer_font.render(timer_data,False,"White")
timer_rect = timer_surface.get_rect(center = (200,50))

pause_button_font = pygame.font.Font("Font/Roboto-Light.ttf",25)
pause_button_surface = pause_button_font.render("Start",False,"White")
pause_button_rect = pause_button_surface.get_rect(topleft = (20,100))
pygame.draw.rect(screen,"White",pause_button_rect,6)

reset_button_font = pygame.font.Font("Font/Roboto-Light.ttf",25)
reset_button_surface = reset_button_font.render("Reset",False,"White")
reset_button_rect =reset_button_surface.get_rect(topleft = (pause_button_rect.right + 25,100))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == timer_event and pause is False:
            second +=1
            if second == 60:
                second = 0
                minute += 1
            if minute == 60:
                minute = 0
                hour += 1
            if hour == 24:
                hour = 0
                day += 1

            timer_data = str(day) + ":" + add_zero_front(hour) + ":" + add_zero_front(minute) + ":" + add_zero_front(second)
            timer_surface = timer_font.render(timer_data,False,"Green")
            timer_rect = timer_surface.get_rect(center = (200,50))
        if pygame.mouse.get_pressed()[0]:
            print("Left click pressed")
            if pause_button_rect.collidepoint(pygame.mouse.get_pos()):
                print("Pause button pressed")
                if pause is True:
                    pause = False
                    timer_surface = timer_font.render(timer_data,False,"Red")
                    pause_button_surface = pause_button_font.render("Pause",False,"White")
                    pause_button_rect = pause_button_surface.get_rect(topleft = (20,100))
                    reset_button_rect =reset_button_surface.get_rect(topleft = (pause_button_rect.right + 25,100))
                else:
                    pause = True
                    timer_surface = timer_font.render(timer_data,False,"Red")
                    pause_button_surface = pause_button_font.render("Continue",False,"White")
                    pause_button_rect = pause_button_surface.get_rect(topleft = (20,100))
                    reset_button_rect =reset_button_surface.get_rect(topleft = (pause_button_rect.right + 25,100))
            if reset_button_rect.collidepoint(pygame.mouse.get_pos()):
                second = 0
                minute = 0
                hour = 0
                day = 0
                pause = True
                timer_data = str(day) + ":" + add_zero_front(hour) + ":" + add_zero_front(minute) + ":" + add_zero_front(second)
                timer_surface = timer_font.render(timer_data,False,"White")
                pause_button_surface = pause_button_font.render("Start",False,"White")
                reset_button_surface = reset_button_font.render("Reset",False,"White")
                
    screen.fill("Black")
    screen.blit(reset_button_surface,reset_button_rect)
    screen.blit(pause_button_surface,pause_button_rect)
    screen.blit(timer_surface,timer_rect)
    pygame.display.update()
    clock.tick(60)