from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
import os


class VideoDownloader:
    def __init__(self, video_url: str, output_path: str, isMP3: bool = False):
        self.__url = video_url
        self.__yt = YouTube(self.__url)
        self.__output_path = output_path
        self.__isMP3 = isMP3

    def __download_video(self):
        stream = self.__yt.streams.get_highest_resolution()
        if self.__isMP3:
            stream = self.__yt.streams.get_audio_only()
        stream.download(output_path=self.__output_path)

    def __convert_to_mp3(self):
        ffmpeg_extract_audio(
            f"{self.__output_path}{self.__yt.title}.mp4",
            f"{self.__output_path}{self.__yt.title}.mp3",
        )

    def __clean_up_video(self):
        os.remove(f"{self.__output_path}{self.__yt.title}.mp4")

    def download(self):
        print("Downloading...")
        self.__download_video()
        if self.__isMP3:
            self.__convert_to_mp3()
            self.__clean_up_video()
        print("Done!")
