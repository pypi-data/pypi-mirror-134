import numpy as np
import cv2 as cv
from typing import List


class Face:
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __getitem__(self, index):
        return (self.x, self.y, self.width, self.height)[index]


def __load_image(image_path: str) -> np.ndarray:
    """
    Loads an image from a file.

    :param image_path: A string specifying where the image in located
    :return: A numpy array of RGB values.
    """
    return cv.imread(image_path)


def __draw_rectangles(image: np.ndarray, faces: List[Face]) -> None:
    if image is None:
        return

    for (x, y, w, h) in faces:
        cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)


def __detect(image: np.ndarray) -> List[Face]:
    """
    Identifies the location of faces in a given numpy array of RGB values.

    :param image: A numpy array of RGB values.
    :return: A list of faces. Each face consists of its x and y coordinates as well as its width and height.
    """
    if image is None:
        return []

    cascade_classifier = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    faces = cascade_classifier.detectMultiScale(gray_image, 1.1, 4)

    return [Face(x, y, w, h) for (x, y, w, h) in faces]


def locate_faces(image_path: str) -> List[Face]:
    """
    Calculates the location of all the faces in a given image.

    :param image_path: A string specifying where the image in located
    :return: A list of faces. Each face consists of its x and y coordinates as well as its width and height.
    """
    image = __load_image(image_path)
    return __detect(image)


def outline_faces(image_path: str) -> None:
    """
    Opens a window displaying the image provided and outlines the faces present in the photo.
    Should be used purely for interactive purposes.

    :param image_path: A string specifying where the image in located.
    :return: None
    """
    image = __load_image(image_path)
    faces = __detect(image)

    __draw_rectangles(image, faces)

    cv.imshow("image", image)
    cv.waitKey(0)
    cv.destroyAllWindows()


def count(image_path: str) -> int:
    """
    Returns the number of faces present in the given image.

    :param image_path: A string specifying where the image in located
    :return: An integer representing the number of `Faces` present.
    """
    image = __load_image(image_path)
    return len(__detect(image))


# For local testing:
# image_path = '../../data/face.jpeg'
# print(count(image_path))
# print(locate_faces(image_path))
# print(outline_faces(image_path))
