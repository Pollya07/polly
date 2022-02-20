import sys
import pygame


def draw(screen):
    screen.fill((0, 0, 0))
    WHITE = (255, 255, 255)
    pygame.draw.line(screen, WHITE, (0, 0), (width, height), width=5)
    pygame.draw.line(screen, WHITE, (0, height), (width, 0), width=5)

    pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    width, height = input().split(" ")
    size = width, height
    try:
        width, height = map(int, size)
        size = width, height
    except ValueError:
        print("Нерпавильный формат ввода")
        sys.exit()
    screen = pygame.display.set_mode(size)
    draw(screen)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
