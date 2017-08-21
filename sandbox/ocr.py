import cv2
from PIL import Image
import pytesseract

from grabscreen import grab_screen


def main():
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
    tessdata_dir_config = '--tessdata-dir "C:/Program Files (x86)/Tesseract-OCR/tessdata"'
    while True:
        screen = grab_screen(region=(880, 675, 950, 705))
        # screen = grab_screen(region=(3, 200, 1020, 800))
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        ret, screen = cv2.threshold(screen, 200, 255, cv2.THRESH_BINARY)
        cv2.imshow('window', screen)
        print('Current speed: {}'.format(pytesseract.image_to_string(Image.fromarray(screen), lang='eng', config = tessdata_dir_config)))

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()
