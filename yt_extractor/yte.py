import argparse
from video_downloader import VideoDownloader
from terminal_utils import print_error


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Download videos from YouTube in MP4 or MP3 format."
    )
    parser.add_argument("url", help="URL of the video to download.")
    parser.add_argument(
        "--path",
        help="Path to store the downloaded file (default: current_directory/out/).",
    )
    parser.add_argument(
        "-mp3", action="store_true", help="Convert the video to MP3 format."
    )
    parser.add_argument(
        "--start-time",
        help="Time from where the video will start (Format: HH:MM:SS [e.g., 00:02:30]).",
    )
    parser.add_argument(
        "--end-time",
        help="Time where the video will end (Format: HH:MM:SS [e.g., 00:05:00]).",
    )
    return parser.parse_args()


def main():
    args = parse_arguments()

    url = args.url
    path = args.path or "./out/"
    mp3 = args.mp3
    start_time = args.start_time
    end_time = args.end_time

    if start_time and not end_time:
        print_error("If a start-time is given, you must specify an end-time.")
        return

    VideoDownloader(
        video_url=url,
        output_path=path,
        start_time=start_time,
        end_time=end_time,
        isMP3=mp3,
    ).download()


if __name__ == "__main__":
    main()
