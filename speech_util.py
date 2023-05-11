
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
                               intro_outro_response_json, interviewer_voice, polly_client):
    q_filenames = []

    # Synthesize the introduction
    filename = synthesize_speech(intro_outro_response_json['Introduction'], interviewer_voice,
                                 'temp/introduction.mp3', polly_client)
    q_filenames.append(filename)

    # Synthesize the questions and answers
    for i in range(1, num_questions):
        question_key = 'Question' + str(i)
        answer_key = 'Answer' + str(i)

        filename = synthesize_speech(response_json[question_key], interviewer_voice,
                                     f'temp/question{i}.mp3', polly_client)
        q_filenames.append(filename)

        filename = synthesize_speech(response_json[answer_key], interviewee_voice,
                                     f'temp/answer{i}.mp3', polly_client)
        q_filenames.append(filename)

    # Synthesize the outro
    filename = synthesize_speech(intro_outro_response_json['Outro'], interviewer_voice,
                                 'temp/outro.mp3', polly_client)
    q_filenames.append(filename)

    return q_filenames