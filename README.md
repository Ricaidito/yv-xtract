# YouTube Video Xtractor

A simple CLI tool to download videos from YouTube either in MP4, MP3 or GIF format and with the ability to crop them.

Developed by [Ricaidito](https://github.com/Ricaidito).

## Usage

```console
yvx [-h] [-mp3] [-gif] [--start-time START_TIME] [--end-time END_TIME] [--path PATH] [--set-path SET_PATH] url

positional arguments:
  url                   URL of the video to download.

options:
  -h, --help            show this help message and exit
  -mp3                  Convert the video to MP3 format.
  -gif                  Convert the video to GIF format.
  --start-time START_TIME
                        Time from where the video will start (Format: HH:MM:SS [e.g., 00:02:30]).
  --end-time END_TIME   Time where the video will end (Format: HH:MM:SS [e.g., 00:05:00]).
  --path PATH           Path to store the downloaded file.
  --set-path SET_PATH   Set the default path to store the downloaded files.
```

### Examples:

To download a video in MP4 format, execute the following command:

```console
yvx <video_url>
```

Download the video in MP3 format:

```console
yvx <video_url> -mp3
```

Download the video in GIF format:

```console
yvx <video_url> -gif
```

To extract a clip from 2:30 to 5:00:

```console
yvx <video_url> --start-time 00:02:30 --end-time 00:05:00
```

You also can specify the end time only. For example, to download the video until 5:00:

```console
yvx <video_url> --end-time 00:05:00
```

## License

This project is licensed under the MIT License.
