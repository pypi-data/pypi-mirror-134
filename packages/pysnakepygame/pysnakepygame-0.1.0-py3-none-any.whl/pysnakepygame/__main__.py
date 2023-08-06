import pygame as pyg
import random
WINDOW_SIZE = 500

class Snake():
    SIZE = 10
    SPEED = 5

    def __init__(self):
        self.body = []
        self.head = None
        self.apple = pyg.Rect(0, 0, Snake.SIZE, Snake.SIZE)
        self.reset()

    def extend(self):
        tail = self.body[-1]
        self.body.append([pyg.Rect(tail[0].left - int(tail[1].x)*Snake.SIZE, tail[0].top - int(tail[1].y)*Snake.SIZE, Snake.SIZE, Snake.SIZE), \
             tail[1]])
        pyg.display.set_caption("Snake | {}".format(len(self.body)))


    def move(self):
        for index, part in reversed(list(enumerate(self.body))):
            part[0].left += Snake.SIZE*int(part[1].x)
            part[0].top  += Snake.SIZE*int(part[1].y)
            if index != 0:
                part[1] = self.body[index - 1][1]

    def check_collisions(self):
        if self.head[0].left <= 0 or self.head[0].top <= 0 or self.head[0].left + Snake.SIZE >= WINDOW_SIZE or self.head[0].top + Snake.SIZE >= WINDOW_SIZE:
            return True
        for index, a in enumerate(self.body):
            for b in self.body[index + 1:len(self.body) - 1]:
                if a[0].colliderect(b[0]):
                    return True
        return False

    def check_keys(self):
        if pyg.key.get_pressed()[pyg.K_UP] and (self.head[1] != pyg.math.Vector2(0, 1) or len(self.body) == 1):
            self.head[1] = pyg.math.Vector2(0, -1)
        elif pyg.key.get_pressed()[pyg.K_DOWN] and (self.head[1] != pyg.math.Vector2(0, -1) or len(self.body) == 1):
            self.head[1] = pyg.math.Vector2(0, 1)
        elif pyg.key.get_pressed()[pyg.K_LEFT] and (self.head[1] != pyg.math.Vector2(1, 0) or len(self.body) == 1):
            self.head[1] = pyg.math.Vector2(-1, 0)
        elif pyg.key.get_pressed()[pyg.K_RIGHT] and (self.head[1] != pyg.math.Vector2(-1, 0) or len(self.body) == 1):
            self.head[1] = pyg.math.Vector2(1, 0)

    def draw(self):
        screen = pyg.display.get_surface()
        for part in self.body:
            pyg.draw.rect(screen, (0, 255, 50), part[0])
        pyg.draw.rect(screen, (255, 0, 0), self.apple)

    def update(self):
        self.check_keys()
        if self.check_collisions():
            self.reset()
        else:
            self.move()
        if self.head[0].colliderect(self.apple):
            self.extend()
            self.move_apple()

    def reset(self):
        self.body = [[pyg.Rect(Snake.SIZE*random.randint(0, WINDOW_SIZE/Snake.SIZE - 1), Snake.SIZE*random.randint(0, WINDOW_SIZE/Snake.SIZE - 1), Snake.SIZE, Snake.SIZE), \
             pyg.math.Vector2(0, 0)]]
        self.head = self.body[0]
        self.move_apple()
        pyg.display.set_caption("Snake | 1")

    def move_apple(self):
        empty = [(x, y) for x, y in zip(range(0, WINDOW_SIZE, Snake.SIZE), range(0, WINDOW_SIZE, Snake.SIZE))]
        for part in self.body:
            try:
                empty.remove((part[0].left, part[0].top))
            except ValueError:
                pass
        self.apple.left, self.apple.top = random.choice(empty)

def main():
    pyg.init()
    screen = pyg.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pyg.display.set_caption("Snake | 1")

    snecc = Snake()

    game_clock = pyg.time.Clock()

    running = True
    while running:
        game_clock.tick(20)

        for event in pyg.event.get():
            if event.type == pyg.QUIT or pyg.key.get_pressed()[pyg.K_ESCAPE]:
                running = False
                break

        screen.fill((0, 0, 0))

        snecc.draw()
        snecc.update()

        pyg.display.flip()

    pyg.quit()

if __name__ == "__main__":
    main()