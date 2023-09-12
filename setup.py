from setuptools import setup, find_packages

setup(
    name="yt_extractor",
    version="1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "yte = yt_extractor.yte:main",
            "yt-extractor = yt_extractor.yte:main",
        ],
    },
)
