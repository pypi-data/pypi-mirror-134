class end_script():
    def end(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            clock.tick()
#start_script.start() fdgdshggfdhjkhsifdajgiudshjfguhdfbshui end_script.end()