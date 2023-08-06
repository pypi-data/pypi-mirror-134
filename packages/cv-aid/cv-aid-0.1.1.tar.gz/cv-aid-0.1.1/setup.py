# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cv_aid', 'tests']

package_data = \
{'': ['*']}

modules = \
['scripts']
install_requires = \
['deepstack-sdk>=0.2.1,<0.3.0', 'filetype>=1.0.9,<2.0.0']

entry_points = \
{'console_scripts': ['test = scripts:test']}

setup_kwargs = {
    'name': 'cv-aid',
    'version': '0.1.1',
    'description': 'CV Aid is a set of helpers of computer vision tasks.',
    'long_description': '# cv-aid\nCV Aid is a set of helpers of computer vision tasks.\n\n## Installation\n\n`pip install cv-aid`\n\n### From source\n\n```\ngit clone https://github.com/khalidelboray/cv-aid\ncd cv-aid\npoetry install\npoetry run python setup.py install\n```\n\n## Tests\n\n`poetry run test`\n\nall tests are in `tests/` directory.\n\n## Examples\n\n- Basic Frame Functions\n\n    ```python\n    from cv_aid import Frame\n\n    frame = Frame.load(\'/path/to/image.jpg\')\n    # or\n    import cv2\n    frame = Frame(cv2.imread(\'/path/to/image.jpg\'))\n\n    # Grayscale image\n    gray = frame.gray()\n\n    # Resize image\n    small = frame.resize(width=100, height=100)\n\n    # Crop image\n    cropped = frame.crop(x=100, y=100, width=100, height=100)\n\n    # All methods return a new Frame object, so you can chain them\n    new_frame = frame.resize(width=100, height=100).crop(x=100, y=100, width=100, height=100)\n\n    # Save image\n    frame.save(\'/path/to/image.jpg\')\n    ```\n\n- Basic Video Functions\n\n    ```python\n    from cv_aid import VideoStream, Frame\n    import cv2\n    import numpy as np\n\n\n    def on_frame(frame: Frame) -> Frame:\n        """\n        A function that is called when a frame is read from the video stream.\n\n        :param frame: The frame that was read.\n        :return: The frame that was read.\n        """\n        orig = frame\n        canny = frame.gray().canny(50, 100)\n        line_image = Frame(np.copy(orig.frame) * 0)\n        lines = cv2.HoughLinesP(\n            canny.frame, 1, np.pi / 180, 50, np.array([]), minLineLength=10, maxLineGap=5\n        )\n        if lines is not None:\n            for line in lines:\n                line = line[0]\n                line_image = line_image.line(\n                    (line[0], line[1]), (line[2], line[3]), (0, 255, 0), 3\n                )\n        lines_edges = cv2.addWeighted(orig.frame, 0.8, line_image.frame, 1, 1)\n        return Frame(lines_edges)\n\n\n    stream = VideoStream(src=0, on_frame=on_frame).start()\n    stream.start_window()\n    ```\n\n    *Output Demo:*\n\n    ![Code Window](/images/stream.png)',
    'author': 'Khalid Mohamed Elborai',
    'author_email': 'accnew820@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/khalidelborai/cv-aid',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
