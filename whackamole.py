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
            mole_row = random.randint(1, grid_rows)
            mole_col = random.randint(1, grid_cols)

            mole_x = mole_col * 32 - mole_width // 2
            mole_y = mole_row * 32 - mole_height // 2

            mole_rect = mole_image.get_rect(center=(mole_x, mole_y))

            screen.fill("light green")
            draw_grid()
            screen.blit(mole_image, mole_rect)
            pygame.display.flip()

            return mole_rect

        mole_rect = mole_image.get_rect(topleft=(0, 0))
        screen.fill("light green")
        draw_grid()
        screen.blit(mole_image, mole_rect)
        pygame.display.flip()
        clock.tick(60)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if (mole_rect.left <= mouse_pos[0] <= mole_rect.right
                            and mole_rect.top <= mouse_pos[1] <= mole_rect.bottom):
                        print("Hit!")
                        mole_rect = move_mole()

    finally:
        pygame.quit()

if __name__ == "__main__":
    main()

