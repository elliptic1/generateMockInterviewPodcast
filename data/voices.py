import random

neural_voices = [

    "Olivia",
    "Aria",
    "Ayanda",
    "Ruth",
    "Stephen",
    "Hala",
    "Zhiyu",
    "Laura",
    "Joey",
    "Amy",

    # "Hiujin",
    # "Emma",
    # "Brian",
    # "Ivy",
    # "Joanna",
    # "Kendra",
    # "Kimberly",
    # "Salli",
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
