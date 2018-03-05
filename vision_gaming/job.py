from vision_gaming.grabber import grab_screen
import time

class Job:

    def __init__(self, screen_rect, process, identify):
        self.screen_rect = screen_rect
        self.process_fcns = process
        self.identify_fcn = identify

    def do(self):
        screen = grab_screen(self.screen_rect)
        for fcn in self.process_fcns:
            screen = fcn(screen)
        result = self.identify_fcn(screen)
        return result
