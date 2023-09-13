from setuptools import setup, find_packages

VERSION = "1.0"
DESCRIPTION = "CLI tool to download youtube videos"
LONG_DESCRIPTION = "A simple CLI tool to download youtube videos either as mp3 or mp4 with the ability to extract clips from the video."

setup(
    name="yt_extractor",
    version=VERSION,
    author="Ricaidito (Ricardo Ramirez)",
    author_email="<ricaiditodev@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["pytube", "moviepy"],
    keywords=["python", "youtube", "video", "downloader", "cli", "mp3", "mp4"],
    entry_points={
        "console_scripts": [
            "yte = yt_extractor.yte:main",
            "yt-extractor = yt_extractor.yte:main",
        ],
    },
)
