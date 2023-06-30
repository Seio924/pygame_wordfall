import pygame

pygame.init()

#화면크기
screen_width = 1440
screen_hight = 900
screen = pygame.display.set_mode((screen_width, screen_hight))

#화면 타이틀
pygame.display.set_caption("WordFall")

#FPS
clock = pygame.time.Clock()
base_font = pygame.font.Font(None, 32)
user_text = ''

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            user_text+=event.unicode

    screen.fill((0, 0, 0))
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface, (0, 0))
    pygame.display.flip()
    clock.tick(60)