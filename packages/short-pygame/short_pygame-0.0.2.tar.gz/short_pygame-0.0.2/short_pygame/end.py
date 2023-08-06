from typing_extensions import Self


class end_script(Self):
    def end(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            clock.tick()
#start_script.start() fdgdshggfdhjkhsifdajgiudshjfguhdfbshui end_script.end()