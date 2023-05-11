import glob
import os
from pydub import AudioSegment


def remove_files():
    if os.path.exists("combined.mp3"):
        os.remove("combined.mp3")
    folder_path = "temp/*"
    files = glob.glob(folder_path)
    for file in files:
        if os.path.isfile(file):
            os.remove(file)


def concatenate_audio_files(all_filenames):
    combined = AudioSegment.empty()

    for filename in all_filenames:
        audio_segment = AudioSegment.from_mp3(filename)
        combined += audio_segment

    # Export the result
    combined.export("combined.mp3", format="mp3")

