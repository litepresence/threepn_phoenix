"""
 ╔════════════════════════════╗
 ║ ╔═╗╔╦╗╔═╗╔═╗╔═╗  ╔╗ ╔═╗╔╦╗ ║
 ║  ╠╣ ║║╠═╝╠╣ ╠═╣  ╠╩╗║ ║ ║  ║
 ║ ╚═╝╚╩╝╩  ╚  ╩ ╩  ╚═╝╚═╝ ╩  ║
 ╚════════════════════════════╝

Gun Detector

WTFPL litepresence 2021

"""

# STANDARD MODULES
import hashlib
import traceback

# THIRD PARTY MODULES
import cv2
import imutils
import matplotlib.pyplot as plt
import numpy as np
import requests
from PIL import Image

# 3DPFA MODULES
from config import DISPLAY, FALSE_CASCADES, TRUE_CASCADES
from text_finder import image_to_text


def download(url):
    """
    download an image url and return the file
    """
    r = requests.get(url, stream=True)
    return Image.open(r.raw).convert("RGB")


def display(true, false, frame):
    for i in true:
        for (x, y, w, h) in true[i]:
            center = (x + w // 2, y + h // 2)
            frame = cv2.ellipse(
                frame, center, (w // 2, h // 2), 0, 0, 360, (0, 255, 0), 4
            )
            frame = cv2.putText(
                frame,
                i.upper().replace("CASCADE_", "").replace(".XML", ""),
                center,
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
            )
    for idx, i in enumerate(false):
        for (x, y, w, h) in false[i]:
            frame = cv2.ellipse(
                frame, center, (w // 2, h // 2), 0, 0, 360, (128, 0, 128), 4
            )
            frame = cv2.putText(
                frame,
                i.upper().replace("CASCADE_", "").replace(".XML", ""),
                center,
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (128, 0, 128),
            )
    plt.imshow(frame)  # , cv2.COLOR_BGR2RGB))
    plt.pause(5)


def multi_haar(cascades, gray_scale, bool_check):
    """
    run multiple haarcascades over the grayscale image, return list of bools
    """
    print("")
    bools = []
    ret = {}
    for cascade_file in cascades:
        try:
            classifier = cv2.CascadeClassifier("haar/" + cascade_file)
            spots = classifier.detectMultiScale(gray_scale, 1.3, 5, minSize=(100, 100))
            detected = bool(len(spots))
            if detected:
                print(cascade_file)
                ret[cascade_file] = spots
            bools.append(detected)
        except Exception:
            print(traceback.format_exc())
    if not bools or not cascades:
        bools.append(not bool_check)
    return bools, ret


def text_check(image, threshold):
    """
    check for more than two 5 letter words
    """
    text = image_to_text(image)
    return text, (len(text.replace(" ", "")) > threshold)


def photo_check(frame, width, threshold):
    """
    ensure enough pixels are unique to be a photo
    """
    frame = imutils.resize(frame, width=width)
    reshaped_frame = frame.reshape(-1, frame.shape[-1])
    colors = np.unique(reshaped_frame, axis=0, return_counts=True)[0]
    print(f"Number of colors in image {len(colors)}")

    return len(colors) > threshold


def detect_gun(img):
    """
    Use haar cascades to see if a gun is present in a PIL image
    """
    meme, is_meme = text_check(img, 10)
    print("MEME:", meme)
    frame = np.asarray(img)
    is_photo = photo_check(frame, width=100, threshold=4000)
    print(50 * "*")
    print(f"IS MEME")
    print(50 * "*")
    print(is_meme)
    print(50 * "*")
    print(f"IS PHOTO")
    print(50 * "*")
    print(is_photo)
    print(50 * "*")
    if is_meme or not is_photo:
        return False, "", is_photo, is_meme, [], []

    frame = imutils.resize(frame, width=1000)
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    print("TRUE CASCADES")
    print(50 * "*")
    true_cascades, true = multi_haar(TRUE_CASCADES, gray_scale, True)
    print(50 * "*")
    print("FALSE CASCADES")
    print(50 * "*")
    false_cascades, false = multi_haar(FALSE_CASCADES, gray_scale, False)
    print(50 * "*")

    if DISPLAY:
        display(true, false, frame)

    thumbnail = str(imutils.resize(frame, width=100))
    hashed_img = hashlib.sha256(thumbnail.encode("utf-8")).hexdigest()
    is_gun = any(true_cascades) and sum([int(b) for b in false_cascades]) <= 2
    print("is_gun", is_gun, hashed_img)
    return (
        is_gun,
        hashed_img,
        is_photo,
        is_meme,
        [int(b) for b in true_cascades],
        [int(b) for b in false_cascades],
    )
