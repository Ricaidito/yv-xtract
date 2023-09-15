from yv_xtract.terminal_utils import (
    parse_arguments,
    print_error,
    print_info,
)
from yv_xtract.yvx_config import YVXConfig
from yv_xtract.video_downloader import VideoDownloader


def main() -> None:
    args = parse_arguments()
    config = YVXConfig()

    url: str = args.url
    given_path: str | None = config.check_path(args.path)
    default_path: str | None = config.check_path(args.set_path)
    mp3: bool = args.mp3
    gif: bool = args.gif
    start_time: str | None = args.start_time
    end_time: str | None = args.end_time

    path_to_save: str = ""

    if mp3 and gif:
        print_error("Cannot convert to MP3 and GIF at the same time.")
        return

    if not config.check_if_config_exists():
        config.create_config_file()

    if default_path is not None:
        config.update_default_path(default_path)

    if given_path is None:
        path_to_save = config.get_default_path()
        print_info(f"Using default path '{path_to_save}' to store the downloaded file.")
    else:
        path_to_save = given_path
        print_info(f"Using '{given_path}' to store the downloaded file.")

    try:
        VideoDownloader(
            video_url=url,
            output_path=path_to_save,
            start_time=start_time,
            end_time=end_time,
            isMP3=mp3,
            isGIF=gif,
        ).download()
    except Exception as err:
        print_error(err)
        return


if __name__ == "__main__":
    main()
