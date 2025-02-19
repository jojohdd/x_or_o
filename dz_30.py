import pygame


pygame.init()


WIDTH, HEIGHT = 300, 300
SQUARE_SIZE = WIDTH // 3
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))

screen.fill(WHITE)


pygame.draw.line(screen, BLACK, (100, 0), (100, 300), 3)
pygame.draw.line(screen, BLACK, (200, 0), (200, 300), 3)
pygame.draw.line(screen, BLACK, (0, 100), (300, 100), 3)
pygame.draw.line(screen, BLACK, (0, 200), (300, 200), 3)


cells = [" "] * 9
player = "X"

running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            index = (y // 100) * 3 + (x // 100)

            if cells[index] == " ":
                cells[index] = player
                cell_x = (index % 3) * 100
                cell_y = (index // 3) * 100

                if player == "X":
                    pygame.draw.line(screen, BLACK, (cell_x + 20, cell_y + 20), (cell_x + 80, cell_y + 80), 3)
                    pygame.draw.line(screen, BLACK, (cell_x + 80, cell_y + 20), (cell_x + 20, cell_y + 80), 3)
                else:
                    pygame.draw.circle(screen, BLACK, (cell_x + 50, cell_y + 50), 30, 3)

                win_patterns = [
                    (0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                    (0, 4, 8), (2, 4, 6)
                ]
                for a, b, c in win_patterns:
                    if cells[a] == cells[b] == cells[c] and cells[a] != " ":
                        print(f"Гравець {player} переміг!")
                        game_over = True

                player = "O" if player == "X" else "X"  # Зміна гравця




    pygame.display.update()

pygame.quit()

