import pygame
import random

# Constants
WIDTH, HEIGHT = 390, 600
CELL_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
COLORS = ["#000000", "#FFD700", "#00FFFF", "#00FF00", "#FFA500", "#FF0000", "#800080", "#0000FF"]  # black, gold, cyan, green, orange, red, purple, blue
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 1], [0, 0, 1]],  # L
    [[1, 1, 1], [1, 0, 0]],  # J
    [[1, 1], [1, 1]],  # O
]

class Tetris:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.clear_lines_sound = pygame.mixer.Sound("clear_lines.wav")
        self.game_over_sound = pygame.mixer.Sound("game over.wav")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_shape = None
        self.current_shape_color = None
        self.current_shape_x = None
        self.current_shape_y = None
        self.particles = []
        self.score = 0
        self.is_game_over = False
        self.spawn_shape()
        self.level = 1

    def draw_grid(self):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                color = COLORS[self.grid[y][x]]
                pygame.draw.rect(self.screen, pygame.Color(color), (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def spawn_shape(self):
        self.current_shape = random.choice(SHAPES)
        self.current_shape_color = random.randint(1, len(COLORS) - 1)
        self.current_shape_x = GRID_WIDTH // 2 - len(self.current_shape[0]) // 2
        self.current_shape_y = 0
        if not self.is_valid_move(0, 0):
            self.end_game()

    def end_game(self):
        self.is_game_over = True
        self.game_over_sound.play()

        font = pygame.font.SysFont("Helvetica", 24)
        game_over_text = font.render("Game Over", True, pygame.Color("white"))
        final_score_text = font.render("Final Score: " + str(self.score), True, pygame.Color("white"))
        level_text = font.render("LEVEL: " + str(self.level), True, pygame.Color("white"))
        play_again_text = font.render("Press Enter to Play Again", True, pygame.Color("white"))
        exit_the_game_text = font.render("Press Space to Exit", True, pygame.Color("white"))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Restart when Enter key is pressed
                        self.__init__()  # Reset the game state
                        return
                    elif event.key == pygame.K_SPACE:  # Exit when Space key is pressed
                        pygame.quit()
                        quit()

            self.screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 100))
            self.screen.blit(final_score_text, (WIDTH // 2 - final_score_text.get_width() // 2, HEIGHT // 2 - 50))
            self.screen.blit(play_again_text, (WIDTH // 2 - play_again_text.get_width() // 2, HEIGHT // 2 + 100))
            self.screen.blit(exit_the_game_text, (WIDTH // 2 - exit_the_game_text.get_width() // 2, HEIGHT // 2 + 50))
            self.screen.blit(level_text, (WIDTH // 2 - level_text.get_width() // 2, HEIGHT // 2))
            pygame.display.flip()
            self.clock.tick(4)

    def is_valid_move(self, dx, dy, shape=None):
        shape = shape or self.current_shape
        for y in range(len(shape)):
            for x in range(len(shape[0])):
                if shape[y][x]:
                    new_x = self.current_shape_x + x + dx
                    new_y = self.current_shape_y + y + dy
                    if not 0 <= new_x < GRID_WIDTH or not 0 <= new_y < GRID_HEIGHT or self.grid[new_y][new_x]:
                        return False
        return True

    def draw_shape(self):
        for y in range(len(self.current_shape)):
            for x in range(len(self.current_shape[0])):
                if self.current_shape[y][x]:
                    color = COLORS[self.current_shape_color]
                    pygame.draw.rect(
                        self.screen,
                        pygame.Color(color),
                        ((self.current_shape_x + x) * CELL_SIZE, (self.current_shape_y + y) * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                    )

    def clear_lines(self):
        lines_to_clear = [i for i, row in enumerate(self.grid) if all(row)]
        if lines_to_clear:
            for line in reversed(lines_to_clear):
                del self.grid[line]
                self.grid.insert(0, [0 for _ in range(GRID_WIDTH)])
                self.score += 10
            self.clear_lines_sound.play()
            for x in range(GRID_WIDTH):
                self.particles.append({
                    "x": x * CELL_SIZE + CELL_SIZE // 2,
                    "y": 0,
                    "speed": random.uniform(1, 3),
                    "angle": random.uniform(0, 360),
                    "size": random.randint(6, 12),
                    "color": random.choice(COLORS),
                    "decay": random.uniform(0.1, 0.5)
                })

    def move_left(self):
        if not self.is_game_over and self.is_valid_move(-1, 0):
            self.current_shape_x -= 1

    def move_right(self):
        if not self.is_game_over and self.is_valid_move(1, 0):
            self.current_shape_x += 1

    def move_down(self):
        if not self.is_game_over:
            if self.is_valid_move(0, 1):
                self.current_shape_y += 1
            else:
                self.place_shape()
                self.clear_lines()
                self.spawn_shape()
                for y in range(len(self.current_shape)):
                    for x in range(len(self.current_shape[0])):
                        if self.current_shape[y][x]:
                            if self.current_shape_y + y < 0:
                                self.is_game_over = True
                                return

    def rotate(self):
        if not self.is_game_over:
            rotated_shape = list(zip(*reversed(self.current_shape)))
            if self.is_valid_move(0, 0, rotated_shape):
                self.current_shape = rotated_shape

    def place_shape(self):
        for y in range(len(self.current_shape)):
            for x in range(len(self.current_shape[0])):
                if self.current_shape[y][x]:
                    self.grid[self.current_shape_y + y][self.current_shape_x + x] = self.current_shape_color

    def is_grid_full(self):
        for row in self.grid:
            if 0 in row:
                return False
        return True

    def update(self):
        self.screen.fill(pygame.Color("black"))
        if self.is_game_over:
            self.end_game()
        else:
            self.draw_grid()
            self.draw_shape()
            self.move_down()

            new_particles = []
            for particle in self.particles:
                particle["y"] += particle["speed"]
                particle["speed"] -= particle["decay"]
                if particle["speed"] > 0:
                    pygame.draw.rect(self.screen, pygame.Color(particle["color"]),
                                     (particle["x"], particle["y"], particle["size"], particle["size"]))
            new_particles.append(particle)
            self.particles = new_particles

            if self.score >= self.level * 10:
                self.level += 1
                pygame.display.flip()
                
            self.clock.tick(2 + self.level)

def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tetris")

    # Load the background image
    try:
        background_image = pygame.image.load("C:\Users\Srivarsha\Downloads\game-music-loop-7-145285.mp3").convert()
    except pygame.error:
        print("Error loading background image.")
        pygame.quit()
        return

    # Load sounds
    try:
        clear_lines_sound = pygame.mixer.Sound("clear_lines.wav")
        starting_sound = pygame.mixer.Sound("Starting.wav")
        starting_sound.play()
    except pygame.error:
        print("Error loading sound files.")
        pygame.quit()
        return

    # Create the start button rectangle
    start_button_rect = pygame.Rect(WIDTH // 2 - 75, HEIGHT // 2 - 25, 150, 50)

    # Game loop
    running = True
    clock = pygame.time.Clock()
    game_started = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    game_started = True
                    starting_sound.stop()

        if not game_started:
            # Display start button and background image
            screen.blit(background_image, (0, 0))

            # Set button color to transparent (alpha = 0)
            transparent = pygame.Color(0, 0, 0)
            pygame.draw.rect(screen, transparent, start_button_rect)
            
            # Create font object for the button label
            font = pygame.font.SysFont("Helvetica", 24)
            button_label = font.render("START", True, pygame.Color("white"))

            # Center the label on the button
            label_x = start_button_rect.centerx - button_label.get_width() // 2
            label_y = start_button_rect.centery - button_label.get_height() // 2

            # Blit the label onto the button
            screen.blit(button_label, (label_x, label_y))
            pygame.display.flip()
        else:
            tetris_game = Tetris()
            while not tetris_game.is_game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            tetris_game.move_left()
                        elif event.key == pygame.K_RIGHT:
                            tetris_game.move_right()
                        elif event.key == pygame.K_DOWN:
                            tetris_game.move_down()
                        elif event.key == pygame.K_SPACE:
                            tetris_game.rotate()

                tetris_game.update()

                # Display level on the screen
                font = pygame.font.SysFont("Helvetica", 28)
                level_text = font.render("LEVEL: " + str(tetris_game.level), True, pygame.Color("white"))
                screen.blit(level_text, (10, 10))
                pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

