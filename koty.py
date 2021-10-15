import requests
import pygame
import sys


def get_cat_fact():
    url = "https://catfact.ninja/fact"
    data = requests.get(url).json()
    fact = data["fact"]
    return fact


def GUI_for_fact():
    text = get_cat_fact()
    pygame.init()
    font = pygame.font.SysFont('Calibri', 15)
    window = pygame.display.set_mode(size=(len(text)*10, 50))
    window.fill((255, 255, 255))
    pygame.display.set_caption("The fact about cats")
    while True:
        pygame.time.delay(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 5 < x < 70 and 20 < y < 40:
                    GUI_for_fact()
        window.blit(font.render(text, True, (0, 0, 0)), (0, 0))
        pygame.draw.rect(window, (128, 128, 128), pygame.Rect(5, 20, 65, 20))
        window.blit(font.render("Next fact", True, (0, 0, 0)), (5, 20))
        pygame.display.flip()


print(GUI_for_fact())