from argparse import Namespace, ArgumentParser
from termcolor import colored


def parse_arguments() -> Namespace:
    parser = ArgumentParser(
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


def print_error(message):
    print(colored(f"[ERROR]: {message}", "red"))


def print_success(message):
    print(colored(f"[SUCCESS]: {message}", "green"))


def print_processing(message):
    print(colored(f"[PROCESSING]: {message}", "yellow"))
