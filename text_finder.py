"""
 ╔════════════════════════════╗
 ║ ╔═╗╔╦╗╔═╗╔═╗╔═╗  ╔╗ ╔═╗╔╦╗ ║
 ║  ╠╣ ║║╠═╝╠╣ ╠═╣  ╠╩╗║ ║ ║  ║
 ║ ╚═╝╚╩╝╩  ╚  ╩ ╩  ╚═╝╚═╝ ╩  ║
 ╚════════════════════════════╝

OCR Meme Detector

WTFPL litepresence 2021
"""

# THIRD PARTY MODULES
import cv2
import numpy as np
import pytesseract


def pre_processing(image):
    """
    This function take one argument as
    input. this function will convert
    input image to binary image
    :param: image
    :return: thresholded image
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    thresholds = []
    for i in [10, 30, 50, 205, 225, 245]:
        thresh = cv2.threshold(blurred, i, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        thresholds.append(thresh)
    return thresholds


def parse_text(image):
    """
    This function take one argument as
    input. this function will feed input
    image to tesseract to predict text.
    :param: image
    return: meta-data dictionary
    """
    # configuring parameters for tesseract
    tesseract_config = r"--oem 3 --psm 6"
    # now feeding image to tesseract
    details = pytesseract.image_to_data(
        image, output_type=pytesseract.Output.DICT, config=tesseract_config, lang="eng"
    )
    text = " ".join(details["text"])
    text = "".join(x for x in text if x.isalpha() or x == " ").rstrip().lstrip()
    text = " ".join([i for i in text.split() if len(i) > 4])
    for i in range(3):
        text = text.replace("  ", " ")
    return text


def image_to_text(image="test"):
    """
    :param: image, or image file name
    return: string of words with 5+ characters
    """
    if isinstance(image, str):
        # reading image from local
        cv2_image = cv2.imread(image)
    else:
        # Convert RGB to BGR
        cv2_image = np.array(image)[:, :, ::-1].copy()
    # calling pre_processing function to perform pre-processing on input image.
    thresholds = pre_processing(cv2_image)
    # calling parse_text function to get text from image by Tesseract.
    text = ""
    for threshold in thresholds:
        text += " " + parse_text(threshold)
    text = " ".join(list(set(text.split())))
    return text.upper()


if __name__ == "__main__":

    print(image_to_text())
