import glob
import os

from pydub import AudioSegment


def remove_files():
    if os.path.exists("output/combined.mp3"):
        os.remove("output/combined.mp3")
    folder_path = "output/temp/*"
    files = glob.glob(folder_path)
    for file in files:
        if os.path.isfile(file):
            os.remove(file)


def concatenate_audio_files(all_filenames):
    combined = AudioSegment.empty()

    for filename in all_filenames:
        audio_segment = AudioSegment.from_mp3(filename)
        random_silence = AudioSegment.silent(duration=1000)
        combined += audio_segment + random_silence

    # Export the result
    combined.export("output/combined.mp3", format="mp3")


def copy_to_google_drive():
    import shutil

    # The source file path
    src_file_path = 'output/final.mp3'

    # The destination directory path
    dest_dir_path = '/Users/toddsmith/Library/CloudStorage/GoogleDrive-elliptic1@gmail.com/My Drive/workspace/podcastMaker/outputs'

    # Combine the destination directory path with the base name of the source file
    dest_file_path = os.path.join(dest_dir_path, os.path.basename(src_file_path))

    # Copy the file
    shutil.copy2(src_file_path, dest_file_path)


def get_article(word):
    return "an" if word[0].lower() in "aeiou" else "a"
