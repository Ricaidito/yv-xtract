# YouTube Video Xtractor

A simple CLI tool to download videos from YouTube either in mp4 or mp3 format and with the ability to crop them.

Developed by [Ricaidito](https://github.com/Ricaidito).

## Usage

```console
yvx [-h] [--path PATH] [-mp3] [--start-time START_TIME] [--end-time END_TIME] [--set-path SET_PATH] url

positional arguments:
  url                   URL of the video to download.

options:
  -h, --help            show this help message and exit
  --path PATH           Path to store the downloaded file (default: current_directory/out/).
  -mp3                  Convert the video to MP3 format.
  --start-time START_TIME
                        Time from where the video will start (Format: HH:MM:SS [e.g., 00:02:30]).
  --end-time END_TIME   Time where the video will end (Format: HH:MM:SS [e.g., 00:05:00]).
  --set-path SET_PATH   Set the default path to store the downloaded files.
```

### Examples:

To download a video, execute the following command:

```console
yvx <video_url>
```

Download the video in mp3 format:

```console
yvx <video_url> -mp3
```

To extract a clip from 2:30 to 5:00:

```console
yvx <video_url> --start-time 00:02:30 --end-time 00:05:00
```

You also can specify the end time only. For example, to download the video until 5:00:

```console
yvx <video_url> --end-time 00:05:00
```

To download the video in a specific directory, you can add the `--path` flag as shown below:

```console
yvx <video_url> --path <path_to_directory>
```

## License

This project is licensed under the MIT License.
