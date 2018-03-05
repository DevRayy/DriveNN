from collections import OrderedDict

import cv2
import pytesseract
from PIL import Image
import numpy as np


def debug_identifier(message):
    def debug_identifier_wrapped(input):
        print(message)
        return message
    return debug_identifier_wrapped


def raw_image():
    def raw_image_wrapped(input):
        return input
    return raw_image_wrapped


def tesseract(exe_path, data_dir, lang='eng'):
    pytesseract.pytesseract.tesseract_cmd = exe_path
    def tesseract_wrapped(input):
        return pytesseract.image_to_string(Image.fromarray(input), lang=lang, config=data_dir)
    return tesseract_wrapped


def match_template(template_image, method=cv2.TM_CCOEFF, show_result=False):
    def match_template_wrapped(input):
        res = cv2.matchTemplate(input, template_image, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if show_result:
            w, h = template_image.shape[::-1]
            top_left = min_loc if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED] else max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            cv2.rectangle(input, top_left, bottom_right, 255, 2)
            cv2.imshow('Template identification', input)
        return max_val, max_loc
    return match_template_wrapped


def match_template_multiple(template_image, threshold=0.9, method=cv2.TM_CCOEFF_NORMED, show_result=False):
    def match_template_multiple_wrapped(input):
        res = cv2.matchTemplate(input, template_image, method)
        loc = np.where(res >= threshold) if method not in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED] else np.where(res <= threshold)
        points = zip(*loc[::-1])
        pts = [(pt[0], pt[1]) for pt in points]
        if show_result:
            w, h = template_image.shape[::-1]
            for pt in pts:
                cv2.rectangle(input, pt, (pt[0]+w, pt[1]+h), 255, 2)
            cv2.imshow('Template identification', input)
        return pts
    return match_template_multiple_wrapped


def match_number(templates, values, threshold=0.85, method=cv2.TM_CCOEFF_NORMED):
    def match_number_wrapped(input):
        fcns = [match_template_multiple(template, threshold, method) for template in templates]
        fvals = [fcn(input) for fcn in fcns]
        x_to_val = {}
        for i in range(len(fvals)): # i = val
            for j in range(len(fvals[i])): # j = point
                x_to_val[fvals[i][j][0]] = values[i]
        digits = [v for v in OrderedDict(sorted(x_to_val.items())).values()]
        digit_count = len(digits)
        result = 0
        for i in range(digit_count):
            result += digits[i] * 10**(digit_count - i - 1)
        return result
    return match_number_wrapped


