import random
from data.get_voices import get_voice_list


def get_interview_voices():
    voice_list = get_voice_list()
    random_name = random.choice(voice_list)
    while random_name == "Arthur":
        random_name = random.choice(voice_list)
    return random_name, "Arthur"
