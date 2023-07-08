from elevenlabs import voices


def get_voice_list():
    voice_data = voices()
    voice_list = list({voice.name for voice in voice_data.voices})
    return voice_list
