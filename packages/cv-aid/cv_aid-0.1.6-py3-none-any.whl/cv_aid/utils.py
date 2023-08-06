# pylint: disable=C0103
__docformat__ = "restructuredtext en"

import base64
import itertools
from pathlib import Path
from typing import Generator, Iterable

import cv2
import filetype
import numpy as np
from deepstack_sdk import ServerConfig


def find_images(path: Path) -> Generator:
    """
    Finds all images in a directory.

    :param path: path to the directory to search in
    :type path: Path
    :return: generator of all images in the directory
    """
    for file in path.iterdir():
        if file.is_dir():
            continue
        if filetype.is_image(file):
            yield file


def find_videos(path: Path) -> Generator:
    """
    Finds all videos in a directory.

    :param path: path to the directory to search in
    :type path: Path
    :return: generator of all videos in the directory
    """
    for file in path.iterdir():
        if file.is_dir():
            continue
        if filetype.is_video(file):
            yield file


def find_fonts(path: Path) -> Generator:
    """
    Finds all fonts in a directory.

    :param path: path to the directory to search in
    :type path: Path
    :return: generator of all fonts in the directory
    """
    for file in path.iterdir():
        if file.is_dir():
            continue
        if filetype.is_font(file):
            yield file


def rotate(img: np.ndarray, angle, center=None, scale=1.0, same_dim=True) -> np.ndarray:
    """
    Rotates an image.

    :param img: image to rotate
    :type img: np.ndarray
    :param angle: angle to rotate the image by
    :type angle: int
    :param center: center of the image to rotate around
    :type center: tuple
    :param scale: scale of the image
    :type scale: float
    :param same_dim: if True, the image will be resized to the same dimensions as the original
    :type same_dim: bool
    :return: rotated image
    """

    if not same_dim:
        return cv2.rotate(img, angle)
    # get the dimensions of the image
    (height, width) = img.shape[:2]

    # if the center is None, initialize it as the center of the image
    if center is None:
        center = (width / 2, height / 2)

    # the rotation
    rota_matrix = cv2.getRotationMatrix2D(center, angle, scale)
    rotated_img = cv2.warpAffine(img, rota_matrix, (width, height))

    # return the rotated image
    return rotated_img


def resize(img: np.ndarray, width, height, inter=cv2.INTER_AREA) -> np.ndarray:
    """
    Resizes an image.

    :param img: image to resize
    :type img: np.ndarray
    :param width: width of the resized image
    :type width: int
    :param height: height of the resized image
    :type height: int
    :param inter: interpolation method
    :type inter: int
    :return: resized image
    """
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        ratio = height / float(height)
        dim = (int(img.shape[1] * ratio), height)
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        ratio = width / float(width)
        dim = (width, int(height * ratio))

    # resize the image
    resized = cv2.resize(img, dim, interpolation=inter)

    return resized


def concatenate(image1: np.ndarray, image2: np.ndarray, axis=1) -> np.ndarray:
    """
    Concatenates two images.

    :param image1: first image to concatenate
    :type image1: np.ndarray
    :param image2: second image to concatenate
    :type image2: np.ndarray
    :param axis: axis to concatenate the images on
    :type axis: int
    :return: concatenated image
    """
    return np.concatenate((image1, image2), axis=axis)


def batch(iterable: Iterable, length: int) -> Generator:
    """
    Batches an iterable.

    :param iterable: iterable to batch
    :type iterable: Iterable
    :param n: number of items to batch
    :type n: int
    :return: generator of batches
    """
    iterator = iter(iterable)
    while item := list(itertools.islice(iterator, length)):
        yield item


def is_type(obj, type_name):
    """
    Checks if an object is of a certain type.

    :param obj: object to check
    :type obj: object
    :param type_name: name of the type to check
    :type type_name: str
    :return: True if the object is of the type, False otherwise
    """
    return type(obj).__name__ == type_name


def verify_frame_type(func):
    """
    Verifies that the frame type is correct.

    :param func: function to decorate
    :type func: function
    :return: decorated function
    """

    def wrapper(self, frame, *args, **kwargs):
        if is_type(frame, "Frame"):
            raise TypeError("The frame must be a Frame object")
        return func(self, frame, *args, **kwargs)

    return wrapper


def copy_frame(func):
    """
    Copies the frame before applying the function.

    :param func: function to decorate
    :type func: function
    :return: decorated function
    """

    def wrapper(*args, **kwargs):
        frame = args[0]
        new_frame = type(frame)(frame.frame.copy())
        return func(new_frame, *args[1:], **kwargs)

    return wrapper


def verify_deepstack_config(func):
    """
    Verifies that the DeepStack config is correct.

    :param func: function to decorate
    :type func: function
    :return: decorated function
    """

    def wrapper(self, *args, **kwargs):
        server_config = kwargs.get("config")
        if server_config is None:
            try:
                server_config = args[1]
            except KeyError:
                raise ValueError(
                    "The server_config must be a ServerConfig object"
                ) from None

        if server_config is None or not isinstance(server_config, ServerConfig):
            raise ValueError("The server_config must be a ServerConfig object")
        if self.server_config.server_url is None:
            raise ValueError("The server_config must have a server_url")

        return func(self, *args, **kwargs)

    return wrapper


class TemplateResponse:
    """
    TemplateResponse class.
    """

    def __init__(self, frame, loc, template):
        """
        Initializes the TemplateResponse class.

        :param frame: frame to apply the template to
        :type frame: np.ndarray
        :param loc: location of the template
        :type loc: tuple
        :param template: template to apply
        :type template: np.ndarray
        """
        self.frame = frame
        self.loc = loc
        self.template = template
        self.width = template.shape[1]
        self.height = template.shape[0]
        self.orig = frame.copy()

    def draw_boxes(self) -> "TemplateResponse":
        """
        Draws the boxes on the frame.

        :return: The resulting TemplateResponse object
        """
        for x, y, width, height, color in self.boxes():
            self.frame = box(self.frame, x, y, width, height, color)
        return self

    def __len__(self):
        return len(self.boxes())

    def __repr__(self):
        return f"TemplateResponse({self.frame})"

    def boxes(self, color=(0, 255, 0)) -> Generator:
        """
        Returns the boxes of the template.

        :param color: color of the boxes
        :type color: tuple
        :return: generator of boxes
        """
        # for x, y in self.loc:
        # yield x, y, self.w, self.h, color
        for point in zip(*self.loc[::-1]):
            yield [
                point[0],
                point[1],
                point[0] + self.width,
                point[1] + self.height,
                color,
            ]


# OpenCV functions


def gray(frame: np.ndarray) -> np.ndarray:
    """
    Converts a color image to grayscale.

    :param frame: image to convert to grayscale
    :type frame: np.ndarray
    :return: grayscale image
    """
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


def crop(frame: np.ndarray, x, y, width, height) -> np.ndarray:
    """
    Crops an image.

    :param frame: image to crop
    :type frame: np.ndarray
    :param x: x coordinate of the top left corner
    :type x: int
    :param y: y coordinate of the top left corner
    :type y: int
    :param w: width of the crop
    :type w: int
    :param h: height of the crop
    :type h: int
    :return: cropped image
    """
    return frame[y : y + height, x : x + width]


def blur(frame: np.ndarray, ksize=(5, 5)) -> np.ndarray:
    """
    Blurs an image.

    :param frame: image to blur
    :type frame: np.ndarray
    :param ksize: size of the kernel
    :type ksize: tuple
    :return: blurred image
    """
    return cv2.blur(frame, ksize=ksize)


def flip(frame: np.ndarray, flip_code=1) -> np.ndarray:
    """
    Flips an image.

    :param frame: image to flip
    :type frame: np.ndarray
    :param flip_code: code for flipping the image
    :type flip_code: int
    :return: flipped image
    """
    return cv2.flip(frame, flip_code)


def line(
    frame: np.ndarray,
    start: tuple,
    end: tuple,
    color=(0, 255, 0),
    thickness=2,
    line_type=cv2.LINE_8,
) -> np.ndarray:
    """
    Draws a line on an image.

    :param frame: image to draw the line on
    :type frame: np.ndarray
    :param start: start point of the line
    :type start: tuple
    :param end: end point of the line
    :type end: tuple
    :param color: color of the line
    :type color: tuple
    :param thickness: thickness of the line
    :type thickness: int
    :param line_type: type of the line
    :type line_type: int
    :return: image with the line
    """
    return cv2.line(frame, start, end, color, thickness, line_type)


def lines(frame, points: list, **kwargs):
    """
    Draws multiple lines on an image.

    :param frame: image to draw the lines on
    :type frame: np.ndarray
    :param points: list of points to draw lines between
    :type points: list
    :param kwargs: keyword arguments for line
    :type kwargs: dict
    :return: image with the lines
    """
    for i in range(len(points) - 1):
        frame = line(frame, points[i][0], points[i][1], **kwargs)
    return frame


def box(
    frame: np.ndarray,
    x,
    y,
    width,
    height,
    color=(0, 255, 0),
    thickness=1,
    line_type=cv2.LINE_8,
    is_max=False,  # pylint: disable=redefined-outer-name
) -> np.ndarray:
    """
    Draws a box on an image.

    :param frame: image to draw the box on
    :type frame: np.ndarray
    :param x: x coordinate of the top left corner
    :type x: int
    :param y: y coordinate of the top left corner
    :type y: int
    :param w: width of the box
    :type w: int
    :param h: height of the box
    :type h: int
    :param color: color of the box
    :type color: tuple
    :param thickness: thickness of the box
    :type thickness: int
    :param line_type: type of the box
    :type line_type: int
    :param max: if True, treat the box as a max box
    :type max: bool
    :return: image with the box
    """
    if is_max:
        frame = cv2.rectangle(
            frame, (x, y), (width, height), color, thickness, line_type
        )
    else:
        frame = cv2.rectangle(
            frame, (x, y), (x + width, y + height), color, thickness, line_type
        )
    return frame


def boxes(frame, cords, **kwargs):
    """
    Draws multiple boxes on an image.

    :param frame: image to draw the boxes on
    :type frame: np.ndarray
    :param cords: list of coordinates of the boxes
    :type cords: list
    :param kwargs: keyword arguments for box
    :type kwargs: dict
    :return: image with the boxes
    """
    for _box in cords:
        frame = box(frame, *_box, **kwargs)
    return frame


def canny(frame: np.ndarray, threshold1=100, threshold2=200) -> np.ndarray:
    """
    Applies Canny edge detection to an image.

    :param frame: image to apply Canny edge detection to
    :type frame: np.ndarray
    :param threshold1: first threshold for Canny edge detection
    :type threshold1: int
    :param threshold2: second threshold for Canny edge detection
    :type threshold2: int
    :return: image with the Canny edge detection applied
    """
    return cv2.Canny(frame, threshold1, threshold2)


def text(
    frame: np.ndarray,
    text_: str,
    x: int,
    y: int,
    font=cv2.FONT_HERSHEY_SIMPLEX,
    scale=0.5,
    color=(0, 255, 0),
    thickness=2,
) -> np.ndarray:
    """
    Draws text on an image.

    :param frame: image to draw the text on
    :type frame: np.ndarray
    :param text_: text to draw
    :type text_: str
    :param x: x coordinate of the top left corner
    :type x: int
    :param y: y coordinate of the top left corner
    :type y: int
    :param font: font to use for the text
    :type font: int
    :param scale: scale of the text
    :type scale: float
    :param color: color of the text
    :type color: tuple
    :param thickness: thickness of the text
    :type thickness: int
    :return: image with the text
    """
    return cv2.putText(frame, text_, (x, y), font, scale, color, thickness, cv2.LINE_AA)


def text_above_box(
    frame: np.ndarray,
    text_: str,
    cords: tuple,
    font=cv2.FONT_HERSHEY_SIMPLEX,
    scale=0.5,
    color=(0, 255, 0),
    thickness=2,
) -> np.ndarray:
    """
    Draws text above a box on an image.

    :param frame: image to draw the text on
    :type frame: np.ndarray
    :param text_: text to draw
    :type text_: str
    :param cords: coordinates of the box
    :type cords: tuple
    :param font: font to use for the text
    :type font: int
    :param scale: scale of the text
    :type scale: float
    :param color: color of the text
    :type color: tuple
    :param thickness: thickness of the text
    :type thickness: int
    :return: image with the text
    """
    return text(
        frame,
        text_,
        cords[0],
        cords[1] - int(scale * 30),
        font,
        scale,
        color,
        thickness,
    )


def search(frame, template, method=cv2.TM_CCOEFF_NORMED, threshold=0.8):
    """
    Searches for a template in an image.

    :param frame: image to search for the template in
    :type frame: np.ndarray
    :param template: template to search for
    :type template: np.ndarray
    :param method: method to use for template matching
    :type method: int
    :param threshold: threshold for template matching
    :type threshold: float
    :return: coordinates of the template in the image
    """
    if is_type(template, "Frame"):
        template = template.frame
    result = cv2.matchTemplate(frame, template, method)
    loc = np.where(result >= threshold)
    return TemplateResponse(frame, loc, template)


def stack(frames: list, resize_=None, cols=2) -> np.ndarray:
    """
    Stacks frames into a single image.

    :param frames: frames to stack
    :type frames: list
    :param resize_: resize the frames
    :type resize_: tuple
    :param cols: number of columns in the stacked image
    :type cols: int
    :return: stacked frames
    """
    min_width = min([frame.shape[1] for frame in frames])
    min_height = min([frame.shape[0] for frame in frames])

    if resize_ is not None:
        min_width = resize_[0]
        min_height = resize_[1]
    # Resize each frame to the minimum width and height
    frames = [resize(frame, min_width, min_height) for frame in frames]

    # Calculate the width and height of the stack by summing the width and height of each frame
    _width = sum([frame.shape[1] for frame in frames])
    _height = sum([frame.shape[0] for frame in frames])
    if cols is not None:
        _width = min_width * cols
        rows_count = int((len(frames) / cols))
        if len(frames) % cols != 0:
            rows_count += 1
        _height = rows_count * min_height

    stacked = np.zeros((_height, _width, 3), np.uint8)

    frames_as_rows = batch(frames, cols)
    for row_index, row in enumerate(frames_as_rows):
        col_index = 0
        for col_index, frame in enumerate(row):
            x = col_index * min_width
            y = row_index * min_height
            stacked[y : y + frame.shape[0], x : x + frame.shape[1]] = frame
        if len(row) < cols:
            # Fill the remaining space with white
            x = (col_index * min_width) + (cols - len(row)) * min_width
            y = row_index * min_height

            stacked[
                y : y + min_height,
                x - (min_width * ((cols - len(row)) - 1)) : x + min_width,
            ] = 255

    return stacked


def to_bytes(frame: np.ndarray) -> bytes:
    """
    Converts a frame to bytes.

    :param frame: frame to convert
    :type frame: np.ndarray
    :return: bytes
    """
    return frame.tobytes()


def to_frame(bytes_: bytes) -> np.ndarray:
    """
    Converts bytes to a frame.

    :param bytes_: bytes to convert
    :type bytes_: bytes
    :return: frame
    """
    return np.frombuffer(bytes_, dtype=np.uint8)


def to_base64(bytes_: bytes) -> str:
    """
    Converts bytes to a base64 string.

    :param bytes_: bytes to convert
    :type bytes_: bytes
    :return: base64 string
    """
    return base64.b64encode(bytes_).decode("utf-8")


def from_base64(base64_: str) -> np.ndarray:
    """
    Converts a base64 string to bytes.

    :param base64_: base64 string to convert
    :type base64_: str
    :return: np.ndarray frame
    """
    return to_frame(base64.b64decode(base64_))
