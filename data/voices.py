import random

neural_voices = [
    # "Hala",
    # "Hiujin",
    # "Zhiyu",
    # "Laura",
    "Olivia",
    # "Amy",
    # "Emma",
    # "Brian",
    "Aria",
    "Ayanda",
    "Kevin",
    "Ruth",
    "Stephen",
    # "Ivy",
    # "Joanna",
    # "Kendra",
    # "Kimberly",
    # "Salli",
    # "Joey",
    # "Matthew",
    # "Suvi",
    # "Lea",
    # "Remi",
    # "Gabrielle",
    # "Liam",
    # "Vicki",
    # "Daniel",
    # "Hannah",
    # "Bianca",
    # "Adriano",
    # "Takumi",
    # "Kazuha",
    # "Ida",
    # "Ola",
    # "Camila",
    # "Vitoria",
    # "Thiago",
    # "Ines",
    # "Lucia",
    # "Sergio",
    # "Mia",
    # "Andres",
    # "Lupe",
    # "Penelope",
    # "Miguel",
    # "Pedro",
    # "Elin"
]


def get_interviewee_voice():
    return random.choice(neural_voices)
