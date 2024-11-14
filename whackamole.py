import pygame, sys
import random

grid_cols = 20
grid_rows = 16
line_color = "black"

def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        mole_width, mole_height = mole_image.get_size()
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        def draw_grid():
            # horizontal lines
            for i in range(1, grid_rows):
                pygame.draw.line(
                    screen,
                    line_color,
                    (0, i*32),
                    (640, i*32)
                )
            # draw vertical lines
            for i in range(1, grid_cols):
                pygame.draw.line(
                    screen,
                    line_color,
                    (i*32, 0),
                    (i*32, 512)
                )

        def move_mole():
            row = random.randint(1, grid_rows)
            col = random.randint(1, grid_cols)
            x = col * 32 - mole_width // 2
            y = row * 32 - mole_height // 2

            mole_coords = (x,y)

            mole_rect = mole_image.get_rect(center=(x, y))

            screen.fill("light green")
            draw_grid()
            screen.blit(mole_image, mole_rect)
            pygame.display.flip()

        #def check_mole_clicked():



        screen.fill("light green")
        draw_grid()
        screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
        pygame.display.flip()
        clock.tick(60)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    move_mole()
                    pygame.display.flip()

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

