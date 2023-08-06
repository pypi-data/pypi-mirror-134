import PIL
from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name="easework",
version="0.6",
description="Python package that makes your work easy",
author="Akul",
author_email="easework25@gmail.com",
packages=['easework'],
install_requires=['pillow','cv2'],
long_description = long_description,
long_description_content_type = "text/markdown",
url = "https://github.com/Dimi-nutive/easework",
)
