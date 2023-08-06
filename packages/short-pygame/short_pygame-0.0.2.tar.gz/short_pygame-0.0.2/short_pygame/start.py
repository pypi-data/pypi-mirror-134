from typing_extensions import Self


class start_script(Self):
    def starting(self):
        pygame.init()
        clock = pygame.time.Clock()
        clock.tick(60)
