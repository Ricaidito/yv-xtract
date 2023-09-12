# YouTube-Extractor

A simple CLI tool to download videos from YouTube either in mp4 or mp3 format.

## Installation

Clone the repository and run the following command in the root directory:

```console
pip install -r requirements.txt
```

**_Note: It is recommended to use a virtual environment to install the dependencies._**

Install the tool locally:

```console
pip install .
```

Or if you plan to make changes to the code, install it in editable mode:

```console
pip install -e .
```

To confirm that the tool is installed, run the one of the following commands:

```console
yt-extractor -h
yte -h
```

## Usage

```console
yt-extractor [-h] [--path PATH] [-mp3] url
yte [-h] [--path PATH] [-mp3] url

positional arguments:
  url          URL of the video to download.

options:
  -h, --help   Show this help message and exit
  --path PATH  Path to store the downloaded file (default: current_directory/out/).
  -mp3         Convert the video to MP3 format.
```

### Examples:

To download a video, run the following command:

```console
yt-extractor <video_url>
```

If you want to download the video in mp3 format, run the following command:

```console
yt-extractor <video_url> -mp3
```

**_Note: Both methods will download the video either in mp4 or mp3 format and store it in a folder named "out" in the tool directory._**

To download the video in a specific directory, run the following command:

```console
yt-extractor <video_url> --path <path_to_directory>
yt-extractor <video_url> --path <path_to_directory> -mp3
```
