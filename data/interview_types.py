import random

interview_types = [
    "technical",
    "systems design",
    "behavioral",
    "product",
    "project management",
    "data science",
    "machine learning",
    "data engineering",
    "data analyst",
    "data visualization",
    "data analytics",
]


def get_interview_type():
    return random.choice(interview_types)
