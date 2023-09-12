from setuptools import setup, find_packages

setup(
    name="yt-extractor",
    version="1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "yt-extractor = yte:main",
            "yte = yte:main",
        ],
    },
)
