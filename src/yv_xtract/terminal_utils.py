from argparse import Namespace, ArgumentParser
from termcolor import colored


def parse_arguments() -> Namespace:
    parser = ArgumentParser(
        description="Download videos from YouTube in MP4, MP3 or GIF format."
    )
    parser.add_argument("url", help="URL of the video to download.")
    parser.add_argument(
        "-mp3", action="store_true", help="Convert the video to MP3 format."
    )
    parser.add_argument(
        "-gif",
        action="store_true",
        help="Convert the video to GIF format.",
    )
    parser.add_argument(
        "--start-time",
        help="Time from where the video will start (Format: HH:MM:SS [e.g., 00:02:30]).",
    )
    parser.add_argument(
        "--end-time",
        help="Time where the video will end (Format: HH:MM:SS [e.g., 00:05:00]).",
    )
    parser.add_argument(
        "--path",
        help="Path to store the downloaded file.",
    )
    parser.add_argument(
        "--set-path",
        help="Set the default path to store the downloaded files.",
    )
    return parser.parse_args()


def print_error(message):
    print(colored(f"[ERROR]: {message}", "red"))


def print_success(message):
    print(colored(f"[SUCCESS]: {message}", "green"))


def print_processing(message):
    print(colored(f"[PROCESSING]: {message}", "yellow"))


def print_info(message):
    print(colored(f"[INFO]: {message}", "blue"))
