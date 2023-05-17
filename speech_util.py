import boto3

from keys import aws_access_key_id, aws_secret_access_key

polly_client = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name='us-east-1'
).client('polly')


def synthesize_speech(text, voice_id, filename):
    response = polly_client.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId=voice_id,
        Engine="neural"
    )
    with open(filename, 'wb') as out:
        out.write(response['AudioStream'].read())
    return filename


def create_intro_audio_files(intro_outro_response_json, interviewee_voice, interviewer_voice):
    # Create a client using the credentials and region defined in your AWS configuration
    return [
        synthesize_speech(intro_outro_response_json['Introduction'],
                          interviewer_voice,
                          'output/temp/introduction.mp3'),
        synthesize_speech(intro_outro_response_json['Guest Intro'],
                          interviewee_voice,
                          'output/temp/guest_introduction.mp3'),
    ]

    # Synthesize the introduction


def create_outro_audio_files(intro_outro_response_json, interviewee_voice, interviewer_voice):
    # Create a client using the credentials and region defined in your AWS configuration
    return [
        synthesize_speech(intro_outro_response_json['Wrap'], interviewer_voice,
                          'output/temp/wrap.mp3'),
        synthesize_speech(intro_outro_response_json['Guest Outro'], interviewee_voice,
                          'output/temp/guest_outro.mp3'),
        synthesize_speech(intro_outro_response_json['Outro'], interviewer_voice,
                          'output/temp/outro.mp3'),
    ]


def create_qa_audio_files(response_json, interviewee_voice, num_questions,
                          interviewer_voice, batch_number):
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
                synthesize_speech(response_json[question_key], interviewer_voice,
                                  f'output/temp/question{batch_number}_{i}.mp3'),
                synthesize_speech(response_json[answer_key], interviewee_voice,
                                  f'output/temp/answer{batch_number}_{i}.mp3'),
                synthesize_speech(response_json[response_key], interviewer_voice,
                                  f'output/temp/response{batch_number}_{i}.mp3')
            ]
        except KeyError:
            print(f"Batch {batch_number} KeyError: " + str(i))

    # Synthesize the outro
    return q_filenames
