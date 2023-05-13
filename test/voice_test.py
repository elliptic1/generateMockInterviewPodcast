import boto3
from IPython.lib.display import Audio

from keys import aws_access_key_id, aws_secret_access_key


def test():
    polly_client = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name='us-east-1'
    ).client('polly')

    response = polly_client.synthesize_speech(
        Text="Create a client using the credentials and region defined in your AWS configuration",
        OutputFormat='mp3',
        VoiceId="Amy",
        Engine="neural"
    )
    with open("test.mp3", 'wb') as out:
        out.write(response['AudioStream'].read())

    Audio("test.mp3", autoplay=True)


if __name__ == "__main__":
    test()
