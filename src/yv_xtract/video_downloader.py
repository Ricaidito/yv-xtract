from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio, ffmpeg_extract_subclip
from yt_extractor.terminal_utils import print_success, print_processing
import os


class VideoDownloader:
    def __init__(
        self,
        video_url: str,
        output_path: str,
        start_time: str = None,
        end_time: str = None,
        isMP3: bool = False,
    ) -> None:
        self.__url = video_url
        self.__yt = YouTube(self.__url)
        self.__current_filename = self.__yt.title
        self.__output_path = output_path
        self.__isMP3 = isMP3
        self.__start_time = start_time
        self.__end_time = end_time

    def __clean_up_default_output_path(self) -> None:
        if os.path.isdir("./out/"):
            if len(os.listdir("./out/")) != 0:
                for file in os.listdir("./out/"):
                    os.remove(f"./out/{file}")

    def __download_video(self) -> None:
        stream = self.__yt.streams.get_highest_resolution()
        if self.__isMP3:
            stream = self.__yt.streams.get_audio_only()
        stream.download(output_path=self.__output_path)

    def __time_to_seconds(self, time: str) -> int:
        h, m, s = map(int, time.split(":"))
        return h * 3600 + m * 60 + s

    def __check_time_in_bounds(self) -> None:
        video_duration = self.__yt.length
        end_time_seconds = self.__time_to_seconds(self.__end_time)

        if end_time_seconds > video_duration:
            self.__clean_up_video()
            raise Exception("End time is greater than video duration.")

    def __cut_video(self) -> None:
        if self.__start_time is None and self.__end_time is None:
            return

        if self.__start_time:
            start_time_parts = list(map(int, self.__start_time.split(":")))
            start_seconds = (
                start_time_parts[0] * 3600
                + start_time_parts[1] * 60
                + start_time_parts[2]
            )
        else:
            start_seconds = 0

        if self.__end_time:
            end_time_parts = list(map(int, self.__end_time.split(":")))
            end_seconds = (
                end_time_parts[0] * 3600 + end_time_parts[1] * 60 + end_time_parts[2]
            )
        else:
            end_seconds = None

        self.__check_time_in_bounds()

        ffmpeg_extract_subclip(
            f"{self.__output_path}{self.__yt.title}.mp4",
            start_seconds,
            end_seconds,
            targetname=f"{self.__output_path}{self.__yt.title}(clip).mp4",
        )
        self.__clean_up_video()
        self.__current_filename = f"{self.__yt.title}(clip)"

    def __convert_to_mp3(self) -> None:
        ffmpeg_extract_audio(
            f"{self.__output_path}{self.__current_filename}.mp4",
            f"{self.__output_path}{self.__current_filename}.mp3",
        )

    def __clean_up_video(self) -> None:
        os.remove(f"{self.__output_path}{self.__current_filename}.mp4")

    def download(self) -> None:
        self.__clean_up_default_output_path()
        print_processing("Downloading video...")
        self.__download_video()
        self.__cut_video()
        if self.__isMP3:
            print_processing("Converting to MP3...")
            self.__convert_to_mp3()
            self.__clean_up_video()
        print_success("Done.")
