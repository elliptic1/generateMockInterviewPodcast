import boto3

from keys import aws_access_key_id, aws_secret_access_key


def synthesize_speech(text, voice_id, filename, polly_client):
    response = polly_client.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId=voice_id,
        Engine="neural"
    )
    with open(filename, 'wb') as out:
        out.write(response['AudioStream'].read())
    return filename


def create_audio_files(response_json, interviewee_voice, num_questions,
                       intro_outro_response_json, interviewer_voice):

    print(response_json)

    # Create a client using the credentials and region defined in your AWS configuration
    polly_client = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name='us-east-1'
    ).client('polly')

    q_filenames = []

    # Synthesize the introduction
    filename = synthesize_speech(intro_outro_response_json['Introduction'], interviewer_voice,
                                 'output/temp/introduction.mp3', polly_client)
    q_filenames.append(filename)
    filename = synthesize_speech(intro_outro_response_json['Guest Intro'], interviewee_voice,
                                 'output/temp/guest_introduction.mp3', polly_client)
    q_filenames.append(filename)

    # Synthesize the questions and answers
    for i in range(1, num_questions):
        question_key = 'Question' + str(i)
        answer_key = 'Answer' + str(i)
        response_key = 'Response' + str(i)

        print("Working on question " + str(i) + "...")

        try:
            filename = synthesize_speech(response_json[question_key], interviewer_voice,
                                         f'output/temp/question{i}.mp3', polly_client)
            q_filenames.append(filename)

            filename = synthesize_speech(response_json[answer_key], interviewee_voice,
                                         f'output/temp/answer{i}.mp3', polly_client)
            q_filenames.append(filename)

            filename = synthesize_speech(response_json[response_key], interviewer_voice,
                                         f'output/temp/response{i}.mp3', polly_client)
            q_filenames.append(filename)
        except KeyError:
            print("KeyError: " + str(i))

    # Synthesize the outro
    filename = synthesize_speech(intro_outro_response_json['Wrap'], interviewer_voice,
                                 'output/temp/wrap.mp3', polly_client)
    q_filenames.append(filename)
    filename = synthesize_speech(intro_outro_response_json['Guest Outro'], interviewee_voice,
                                 'output/temp/guest_outro.mp3', polly_client)
    q_filenames.append(filename)
    filename = synthesize_speech(intro_outro_response_json['Outro'], interviewer_voice,
                                 'output/temp/outro.mp3', polly_client)
    q_filenames.append(filename)

    return q_filenames
