import settings
from maze import Maze
from tasks import tasks
from tasks.tasks import greetings
from ui import events
from ui import graphics

FPS = 60
running = True
clock = events.Clock()

# Приветствие. Его нужно удалить
greetings()

while running:
    for event in events.get_event_queue():
        if tasks.handle_event(event):
            continue
        if event.type == events.QUIT:
           running = False
        if event.type == events.MOUSEBUTTONDOWN:
            if event.button == 1:
                Maze.add_mouse(event.pos[0], event.pos[1])

    graphics.fill("black")
    # рисуем лабиринт
    Maze.draw()
    tasks.check_tasks()
    graphics.flip()
    clock.tick(FPS)
    # обновляем весь лабиринт
    Maze.update(1 / FPS)
