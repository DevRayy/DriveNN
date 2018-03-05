from grabscreen import grab_screen
from PIL import Image
import pytesseract
import settings
import cv2


class Speedometer:
    def __init__(self):
        self.speed = 0
        self.acceleration = 0
        pytesseract.pytesseract.tesseract_cmd = 'C:/Soft/Tesseract-OCR/tesseract.exe'
        self._tessdata_dir_config = '--tessdata-dir "C:/Soft/Tesseract-OCR/tessdata"'

    def run(self):
        while True:
            try:
                speed_screen = grab_screen(region=settings.SPEED_BOUNDARIES)
                speed_screen = cv2.cvtColor(speed_screen, cv2.COLOR_BGR2GRAY)
                ret, speed_screen = cv2.threshold(speed_screen, 200, 255, cv2.THRESH_BINARY)
                speed = pytesseract.image_to_string(Image.fromarray(speed_screen), lang='eng', config=self._tessdata_dir_config)
                try:
                    old_speed = self.speed
                    self.speed = int(speed) / 100.0
                    self.acceleration = (self.speed - old_speed) / 25.0
                except:
                    pass
            except:
                pass

    def get(self):
        return [self.speed, self.acceleration]
