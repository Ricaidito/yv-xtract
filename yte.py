import argparse
from video_downloader import VideoDownloader


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
    return parser.parse_args()


def main():
    args = parse_arguments()

    url = args.url
    path = args.path or "./out/"
    mp3 = args.mp3

    VideoDownloader(
        video_url=url,
        output_path=path,
        isMP3=mp3,
    ).download()


if __name__ == "__main__":
    main()
