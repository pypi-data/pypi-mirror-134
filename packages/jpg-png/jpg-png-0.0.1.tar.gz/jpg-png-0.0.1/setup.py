import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="jpg-png",
    version="0.0.1",
    description="It converts jpg formated images to png formate",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/AhzamAhmed6/JPG_to_PNG_converter",
    author="Ahzam Ahmed",
    author_email="ahzamahmed6@gmail.com.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["jpg-png"],
    include_package_data=True,
    install_requires=['pillow'],
    # entry_points={
    #     "console_scripts": [
    #         "jpg-png=jpg-png.__main__:main",
    #     ]
    # },
)