# cv-aid

CV Aid is a set of helpers of computer vision tasks.

## Installation

`pip install cv-aid`

### From source

```
git clone https://github.com/khalidelboray/cv-aid
cd cv-aid
poetry install
poetry run python setup.py install
```

## Tests

`poetry run test`

all tests are in `tests/` directory.

## Examples

- Basic Frame Functions

    ```python
    from cv_aid import Frame

    frame = Frame.load('/path/to/image.jpg')
    # or
    import cv2
    frame = Frame(cv2.imread('/path/to/image.jpg'))

    # Grayscale image
    gray = frame.gray()

    # Resize image
    small = frame.resize(width=100, height=100)

    # Crop image
    cropped = frame.crop(x=100, y=100, width=100, height=100)

    # All methods return a new Frame object, so you can chain them
    new_frame = frame.resize(width=100, height=100).crop(x=100, y=100, width=100, height=100)

    # Save image
    frame.save('/path/to/image.jpg')
    ```

- Basic Video Functions

    ```python
    from cv_aid import VideoStream, Frame
    import cv2
    import numpy as np


    def on_frame(frame: Frame) -> Frame:
        """
        A function that is called when a frame is read from the video stream.

        :param frame: The frame that was read.
        :return: The frame that was read.
        """
        orig = frame
        canny = frame.gray().canny(50, 100)
        line_image = Frame(np.copy(orig.frame) * 0)
        lines = cv2.HoughLinesP(
            canny.frame, 1, np.pi / 180, 50, np.array([]), minLineLength=10, maxLineGap=5
        )
        if lines is not None:
            for line in lines:
                line = line[0]
                line_image = line_image.line(
                    (line[0], line[1]), (line[2], line[3]), (0, 255, 0), 3
                )
        lines_edges = cv2.addWeighted(orig.frame, 0.8, line_image.frame, 1, 1)
        return Frame(lines_edges)


    stream = VideoStream(src=0, on_frame=on_frame).start()
    stream.start_window()
    ```

    *Output Demo:*

    ![Code Window](https://raw.githubusercontent.com/khalidelboray/cv-aid/master/images/stream.png)

- Haar Cascade Functions

    ```python
    from cv_aid import VideoStream, Frame

    def on_frame(frame: Frame) -> Frame:
        """
        A function that is called when a frame is read from the video stream.

        :param frame: The frame that was read.
        :return: The frame that was read.
        """
        boxes = frame.haarcascades.detect_faces(frame.frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        frame = frame.boxes(boxes, color=(0, 255, 0))
        return frame


    if __name__ == "__main__":

        stream = VideoStream(src=0, on_frame=on_frame).start()
        stream.start_window()
    ```

    *Output Demo:*

    ![haarcascade Window](https://raw.githubusercontent.com/khalidelboray/cv-aid/master/images/haarcascade.png)

- Tourch Hub (Yolov5)

    ```python
    from cv_aid import VideoStream, Frame
    import torch

    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

    def on_frame(frame: Frame) -> Frame:
        """
        A function that is called when a frame is read from the video stream.

        :param frame: The frame that was read.
        :return: The frame that was read.
        """
        results = model(frame.frame)
        results.display(render=True)
        frame = Frame(results.imgs[0])    
        return frame


    if __name__ == "__main__":
        
        stream = VideoStream(src=0, on_frame=on_frame).start()
        stream.start_window()
    ```

    ![torch yolov5](https://raw.githubusercontent.com/khalidelboray/cv-aid/master/images/torch_yolo.png)
