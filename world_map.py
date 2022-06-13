import pygame as p
import os
import sys

p.font.init()
p.init

WIDTH, HEIGHT = 1000, 600
FPS = 60

WORLD_MAP = p.image.load(os.path.join("assets", "map.jpg"))
WORLD = p.transform.scale(WORLD_MAP, (WIDTH, HEIGHT))

WIN = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption("World Map")


class Country:
    def __init__(self, country_name: str, file_name: str, size: tuple, pos: tuple) -> None:
        self.size = size
        self.pos = pos
        self.country_name = country_name
        self.file_name = file_name
        self.COUNTRY = p.image.load(os.path.join("assets", file_name))
        self.COUN = p.transform.scale(self.COUNTRY,size)
        self.display_name = p.font.SysFont("monospace", 10)
    
    
    def update(self):
        WIN.blit(self.COUN, self.pos)
        if self.pos[0] < p.mouse.get_pos()[0] and self.pos[0] + self.size[0] > p.mouse.get_pos()[0] and self.pos[1] < p.mouse.get_pos()[1] and self.pos[1] + self.size[1] > p.mouse.get_pos()[1]:
            self.name_display = self.display_name.render(self.country_name, 1, (0,0,0))
            WIN.blit(self.name_display, self.pos)
        


United_States = Country("United States", "United_States2.png",(156, 95), (140, 210))     


def main():
    run = True
    clock = p.time.Clock()
    while run:
        clock.tick(FPS)
        for e in p.event.get():
            if e.type == p.QUIT:
                p.quit()
                sys.exit(1)
        
        WIN.blit(WORLD,(0,0))
        United_States.update()
        p.display.update()
    p.quit()           


if __name__ == "__main__":
    main()           
