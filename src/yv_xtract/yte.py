from yv_xtract.terminal_utils import parse_arguments, print_error
from yv_xtract.video_downloader import VideoDownloader


def main() -> None:
    args = parse_arguments()

    url: str = args.url
    path: str = args.path or "./out/"
    mp3: bool = args.mp3
    start_time: str = args.start_time
    end_time: str = args.end_time

    if start_time and not end_time:
        print_error("If a start-time is given, you must specify an end-time.")
        return

    try:
        VideoDownloader(
            video_url=url,
            output_path=path,
            start_time=start_time,
            end_time=end_time,
            isMP3=mp3,
        ).download()
    except Exception as err:
        print_error(err)
        return


if __name__ == "__main__":
    main()
