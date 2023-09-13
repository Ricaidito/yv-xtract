# YouTube_Extractor

A simple CLI tool to download videos from YouTube either in mp4 or mp3 format and with the ability to crop them.

## Local installation

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
```

## Usage

```console
yt-extractor [-h] [--path PATH] [-mp3] [--start-time START_TIME] [--end-time END_TIME] url

OR

yte [-h] [--path PATH] [-mp3] [--start-time START_TIME] [--end-time END_TIME] url

positional arguments:
  url                   URL of the video to download.

options:
  -h, --help            show this help message and exit
  --path PATH           Path to store the downloaded file (default: current_directory/out/).
  -mp3                  Convert the video to MP3 format.
  --start-time START_TIME
                        Time from where the video will start (Format: HH:MM:SS [e.g., 00:02:30]).
  --end-time END_TIME   Time where the video will end (Format: HH:MM:SS [e.g., 00:05:00]).
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

You can also extract a clip from the video by specifying the start and end time of the clip. For example, to extract a clip from 2:30 to 5:00, run the following command:

```console
yt-extractor <video_url> --start-time 00:02:30 --end-time 00:05:00
```

And if you want the video only until certain time, you can specify the end time only. For example, to download the video until 5:00, run the following command:

```console
yt-extractor <video_url> --end-time 00:05:00
```

**_Note: All methods shown here will download the video either in mp4 or mp3 format and store it in a folder named "out" in the tool directory._**

To download the video in a specific directory, you can add the `--path` flag as shown below:

```console
yt-extractor <video_url> --path <path_to_directory>
```
