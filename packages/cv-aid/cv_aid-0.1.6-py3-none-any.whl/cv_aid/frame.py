# pydoctor --project-base-dir=. --make-html --docformat=restructuredtext cv_aid/
# pylint: disable=C0103
__docformat__ = "restructuredtext en"

import os
import cv2
import numpy as np

from cv_aid import utils
from cv_aid.haarcascades import Haarcascades


class Frame:  # pylint: disable=too-many-public-methods
    """A class to represent a frame of video."""

    def __init__(self, frame):
        """Initialize a Frame object.

        :param frame: The frame to be represented.
        :type frame: numpy.ndarray
        """
        self.frame = frame
        self.original_frame = frame.copy()
        self._haarcascades = None

    @classmethod
    def load(cls, path) -> "Frame":
        """Load a frame from a file.

        :param path: Path to the file.
        :type path: str
        """
        return cls(cv2.imread(str(path)))

    @property
    def shape(self) -> tuple:
        """Get the shape of the frame."""
        return self.frame.shape

    @property
    def width(self) -> int:
        """Get the width of the frame."""
        return self.shape[1]

    @property
    def height(self) -> int:
        """Get the height of the frame."""
        return self.shape[0]

    @property
    def size(self) -> int:
        """Get the size of the frame."""
        return self.shape[:2]

    @property
    def channels(self) -> int:
        """Get the number of channels in the frame."""
        return self.shape[2]

    def to_bytes(self) -> bytes:
        """Convert the frame to bytes.

        :return: The resulting bytes.
        """
        return self.frame.tobytes()

    def gray(self) -> "Frame":
        """Convert the frame to grayscale.

        :return: The resulting frame.
        """
        return Frame(utils.gray(self.frame))

    def resize(self, width=None, height=None, inter=cv2.INTER_AREA) -> "Frame":
        """Resize the frame.

        :param width: The new width.
        :type width: int
        :param height: The new height.
        :type height: int
        :param inter: The interpolation method.
        :type inter: int
        :return: The resulting frame.
        """
        return Frame(utils.resize(self.frame, width, height, inter))

    def rotate(self, angle, center=None, scale=1.0, same_dim=True) -> "Frame":
        """Rotate the frame.

        :param angle: The angle to rotate the frame by.
        :type angle: float
        :param center: The center of rotation.
        :type center: tuple
        :param scale: The scale to apply.
        :type scale: float
        :return: The resulting frame.
        """
        return Frame(utils.rotate(self.frame, angle, center, scale, same_dim))

    def flip(self, flip_code) -> "Frame":
        """Flip the frame.

        :param flip_code: The code for the flip.
        :type flip_code: int
        :return: The resulting frame.
        """
        return Frame(utils.flip(self.frame, flip_code))

    def crop(self, x, y, width, height) -> "Frame":  # pylint: disable=invalid-name
        """Crop the frame.

        :param x: The x coordinate of the top left corner.
        :type x: int
        :param y: The y coordinate of the top left corner.
        :type y: int
        :param width: The width of the crop.
        :type width: int
        :param height: The height of the crop.
        :type height: int
        :return: The resulting frame.
        """
        return Frame(utils.crop(self.frame, x, y, width, height))

    def crop_to_size(self, width, height) -> "Frame":
        """Crop the frame to a specific size.

        :param width: The width of the frame.
        :type width: int
        :param height: The height of the frame.
        :type height: int
        :return: The resulting frame.
        """
        return self.crop(0, 0, width, height)

    def crop_to_ratio(self, ratio) -> "Frame":
        """Crop the frame to a specific ratio.

        :param ratio: The ratio to crop to.
        :type ratio: float
        :return: The resulting frame.
        """
        return self.crop_to_size(int(self.width / ratio), int(self.height / ratio))

    def crop_to_ratio_width(self, ratio) -> "Frame":
        """Crop the frame to a specific ratio.

        :param ratio: The ratio to crop to.
        :type ratio: float
        :return: The resulting frame.
        """
        return self.crop_to_size(int(self.width / ratio), self.height)

    def crop_to_ratio_height(self, ratio) -> "Frame":
        """Crop the frame to a specific ratio.

        :param ratio: The ratio to crop to.
        :type ratio: float
        :return: The resulting frame.
        """
        return self.crop_to_size(self.width, int(self.height / ratio))

    def blur(self, ksize=5) -> "Frame":
        """Blur the frame.

        :param ksize: The kernel size.
        :type ksize: int
        :return: The resulting frame.
        """
        return Frame(utils.blur(self.frame, ksize))

    def canny(self, threshold1, threshold2) -> "Frame":
        """Apply the Canny edge detector.

        :param threshold1: The first threshold.
        :type threshold1: int
        :param threshold2: The second threshold.
        :type threshold2: int
        :return: The resulting frame.
        """
        return Frame(utils.canny(self.frame, threshold1, threshold2))

    def line(
        self, start, end, color=(0, 255, 0), thickness=1, line_type=cv2.LINE_8
    ) -> "Frame":
        """Draw a line on the frame.

        :param start: The start of the line.
        :type start: tuple
        :param end: The end of the line.
        :type end: tuple
        :param color: The color of the line.
        :type color: tuple
        :param thickness: The thickness of the line.
        :type thickness: int
        :param line_type: The type of the line.
        :type line_type: int
        :return: The resulting frame.
        """
        return Frame(utils.line(self.frame, start, end, color, thickness, line_type))

    def box(
        self,
        x,
        y,
        width,
        height,
        color,
        thickness=1,
        line_type=cv2.LINE_8,  # pylint: disable=invalid-name
        is_max=False,
    ) -> "Frame":
        """Draw a box on the frame.

        :param x: The x coordinate of the top left corner.
        :type x: int
        :param y: The y coordinate of the top left corner.
        :type y: int
        :param width: The width of the box.
        :type width: int
        :param height: The height of the box.
        :type height: int
        :param color: The color of the box.
        :type color: tuple
        :param thickness: The thickness of the box.
        :type thickness: int
        :param line_type: The type of the box.
        :type line_type: int
        :return: The resulting frame.
        """
        return Frame(
            utils.box(
                self.frame,
                x,
                y,
                width,
                height,
                color,
                thickness,
                line_type,
                is_max=is_max,
            )
        )

    def lines(self, points, color, thickness=1, line_type=cv2.LINE_8) -> "Frame":
        """Draw lines on the frame.

        :param points: The points to draw.
        :type points: List[Tuple[int, int]]
        :param color: The color of the lines.
        :type color: tuple
        :param thickness: The thickness of the lines.
        :type thickness: int
        :param line_type: The type of the lines.
        :type line_type: int
        :return: The resulting frame.
        """
        return Frame(
            utils.lines(
                self.frame,
                points,
                color=color,
                thickness=thickness,
                line_type=line_type,
            )
        )

    def boxes(
        self, boxes, color, thickness=1, line_type=cv2.LINE_8, is_max=False
    ) -> "Frame":
        """Draw boxes on the frame.

        :param boxes: The boxes to draw.
        :type boxes: List[Tuple[int, int, int, int]]
        :param color: The color of the boxes.
        :type color: tuple
        :param thickness: The thickness of the boxes.
        :type thickness: int
        :param line_type: The type of the boxes.
        :type line_type: int
        :return: The resulting frame.
        """
        return Frame(
            utils.boxes(
                self.frame,
                boxes,
                color=color,
                thickness=thickness,
                line_type=line_type,
                is_max=is_max,
            )
        )

    def text(
        self,
        text,
        position,
        font_face=cv2.FONT_HERSHEY_SIMPLEX,
        font_scale=1.0,
        color=(0, 255, 0),
        thickness=1,
    ) -> "Frame":
        """Draw text on the frame.

        :param text: The text to draw.
        :type text: str
        :param position: The position of the text.
        :type position: tuple
        :param color: The color of the text.
        :type color: tuple
        :param font_face: The font face of the text.
        :type font_face: int
        :param font_scale: The font scale of the text.
        :type font_scale: float
        :param thickness: The thickness of the text.
        :type thickness: int
        :return: The resulting frame.
        """
        return Frame(
            utils.text(
                self.frame,
                text,
                *position,
                font_face,
                font_scale,
                color,
                thickness,
            )
        )

    def __add__(self, other) -> "Frame":
        """Add two frames together.

        :param other: The other frame to be added.
        :type other: Frame
        :return: The resulting frame.
        """
        return Frame(self.frame + other.frame)

    def __sub__(self, other) -> "Frame":
        """Subtract two frames.

        :param other: The other frame to be subtracted.
        :type other: Frame
        :return: The resulting frame.
        """
        return Frame(self.frame - other.frame)

    def __mul__(self, other) -> "Frame":
        """Multiply two frames.

        :param other: The other frame to be multiplied.
        :type other: Frame
        :return: The resulting frame.
        """
        return Frame(self.frame * other.frame)

    def __truediv__(self, other) -> "Frame":
        """Divide two frames.

        :param other: The other frame to be divided.
        :type other: Frame
        :return: The resulting frame.
        """
        return Frame(self.frame / other.frame)

    def abs(self) -> "Frame":
        """Take the absolute value of the frame.

        :return: The resulting frame.
        """
        return Frame(np.abs(self.frame))

    def show(self, title="Frame") -> None:
        """Show the frame.

        :param title: The title of the frame.
        :type title: str
        """
        cv2.imshow(title, self.frame)

    def save(self, path, name):
        """Save the frame.

        :param path: The path to save the frame.
        :type path: str
        :param name: The name of the frame.
        :type name: str
        """
        cv2.imwrite(os.path.join(path, name), self.frame)

    def __repr__(self) -> str:
        """Get the string representation of the frame.

        :return: The string representation of the frame.
        """
        return f"Frame({self.frame.shape})"

    @property
    def haarcascades(self):
        """Provides access to the haarcascades."""
        # Create the haarcascades class if it doesn't exist
        if not hasattr(self, "_haarcascades") or getattr(self, "_haarcascades") is None:
            self._haarcascades = Haarcascades()
        return self._haarcascades
