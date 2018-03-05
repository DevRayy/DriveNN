import cv2


def show_screen(name):
    def show_screen_wrapped(screen):
        cv2.imshow(name, screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
        return screen

    return show_screen_wrapped


def resize(new_size):
    def resize_wrapped(screen):
        return cv2.resize(screen, new_size)
    return resize_wrapped


def convert_color(converter):
    def convert_color_wrapped(screen):
        return cv2.cvtColor(screen, converter)
    return convert_color_wrapped


def binary_threshold(thresh, max):
    def binary_threshold_wrapped(screen):
        return (cv2.threshold(screen, thresh, max, cv2.THRESH_BINARY))[1]
    return binary_threshold_wrapped
