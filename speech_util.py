import json

import requests
from elevenlabs import generate


def synthesize_speech(text, voice_name, filename):
    audio = generate(
        text=text,
        voice=voice_name,
        model='eleven_monolingual_v1'
    )

    with open(filename, 'wb') as out:
        out.write(audio)
    return filename


def create_intro_audio_files(intro_outro_response_json, interviewee_voice_name, interviewer_voice_name):
    # Create a client using the credentials and region defined in your AWS configuration
    return [
        synthesize_speech(intro_outro_response_json['Introduction'],
                          interviewer_voice_name,
                          'output/temp/introduction.mp3'),
        synthesize_speech(intro_outro_response_json['Guest Intro'],
                          interviewee_voice_name,
                          'output/temp/guest_introduction.mp3'),
    ]

    # Synthesize the introduction


def create_outro_audio_files(intro_outro_response_json, interviewee_voice_name, interviewer_voice_name):
    # Create a client using the credentials and region defined in your AWS configuration
    return [
        synthesize_speech(intro_outro_response_json['Wrap'], interviewer_voice_name,
                          'output/temp/wrap.mp3'),
        synthesize_speech(intro_outro_response_json['Guest Outro'], interviewee_voice_name,
                          'output/temp/guest_outro.mp3'),
        synthesize_speech(intro_outro_response_json['Outro'], interviewer_voice_name,
                          'output/temp/outro.mp3'),
    ]


def create_qa_audio_files(response_json, interviewee_voice_name, num_questions,
                          interviewer_voice_name, batch_number):
    print(response_json)

    # Create a client using the credentials and region defined in your AWS configuration
    q_filenames = []

    # Synthesize the questions and answers
    for i in range(1, num_questions + 1):
        question_key = 'Question' + str(i)
        answer_key = 'Answer' + str(i)
        response_key = 'Response' + str(i)

        print(f"Working on batch {batch_number}, question {i}...")

        try:
            q_filenames += [
                synthesize_speech(response_json[question_key], interviewer_voice_name,
                                  f'output/temp/question{batch_number}_{i}.mp3'),
                synthesize_speech(response_json[answer_key], interviewee_voice_name,
                                  f'output/temp/answer{batch_number}_{i}.mp3'),
                synthesize_speech(response_json[response_key], interviewer_voice_name,
                                  f'output/temp/response{batch_number}_{i}.mp3')
            ]
        except KeyError:
            print(f"Batch {batch_number} KeyError: " + str(i))

    # Synthesize the outro
    return q_filenames
