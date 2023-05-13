from pydub import AudioSegment


def add_intro_outro_music():
    # Load the two audio files
    voices = AudioSegment.from_file("output/combined.mp3")
    music = AudioSegment.from_file("music/music.mp3")

    # Ensure music is not louder than voices
    music = music - 20  # Reduces music's volume by 10 dB

    # Use 25 seconds of music for intro
    music_intro = music[:25 * 1000]  # Length in milliseconds

    # Fade music intro in over 5 seconds and fade out over 5 seconds
    music_intro = music_intro.fade_in(5 * 1000).fade_out(15 * 1000)

    # Prepend 5 seconds of silence to voices
    silence = AudioSegment.silent(duration=5 * 1000)
    end_silence = AudioSegment.silent(duration=20 * 1000)
    full = silence + voices + end_silence

    # Overlay music intro on top of voices, starting at 0 seconds
    full = full.overlay(music_intro, position=0)

    # Use 30 seconds of music for outro
    music_outro = music[:30 * 1000]  # Length in milliseconds

    # Fade music outro in over 10 seconds
    music_outro = music_outro.fade_in(10 * 1000).fade_out(10 * 1000)

    full_duration = len(full)  # Get duration in milliseconds
    music_outro_start_time = full_duration - 30 * 1000  # Start 10 seconds before voices end

    # Overlay the music outro at the specific start time
    full = full.overlay(music_outro, position=music_outro_start_time)

    # Save the result
    full.export("output/final.mp3", format="mp3")
