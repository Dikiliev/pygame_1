import pygame


class Board:
    # создание поля
    def __init__(self, width, height, left=10, top=10, cell_size=30):
        self.width = width
        self.height = height
        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.board = [[1] * width for _ in range(height)]

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, (255, 255, 255),
                                 [(self.left + (j * self.cell_size), self.top + (i * self.cell_size)),
                                  (self.cell_size, self.cell_size)], self.board[i][j])

    def get_cell(self, mouse_pos):
        for i in range(self.width):
            cell_x = self.left + (self.cell_size * i)
            for j in range(self.height):
                cell_y = self.top + (self.cell_size * j)
                if cell_x < mouse_pos[0] < cell_x + self.cell_size and cell_y < mouse_pos[1] < cell_y + self.cell_size:
                    return j, i

    def on_click(self, cell_pos):
        row, col = cell_pos
        print(row, col)
        for i in range(self.width):
            self.board[row][i] ^= 1
        for j in range(self.height):
            self.board[j][col] ^= 1
        self.board[row][col] ^= 1
        print(self.board[row][col])

    def get_click(self, mouse_pos):
        cell_pos = self.get_cell(mouse_pos)
        if cell_pos:
            self.on_click(cell_pos)


def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    clock = pygame.time.Clock()
    board = Board(5, 7)

    FPS = 50

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        board.render(screen)

        pygame.display.flip()
        screen.fill((0, 0, 0))
        clock.tick(FPS)


if __name__ == '__main__':
    main()
