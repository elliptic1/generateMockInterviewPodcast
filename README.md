# Interview Podcast Generator

Interview Podcast Generator is a Python application that uses OpenAI's GPT model for generating mock interviews in a podcast format. The project also utilizes Amazon Polly to generate audio from the generated text.

## Features

- Utilizes OpenAI's GPT model for generating interview content
- Uses Amazon Polly to generate audio from the interview content
- Generates structured interviews, including introduction, questions and answers, and outro
- Customizable interview structure and content

## Installation

1. Clone this repository:
`git clone https://github.com/yourusername/interviewPodcastGenerator.git`

2. Install the dependencies:
`pip install -r requirements.txt`

Please ensure you have the latest versions of boto3 and botocore.

## Usage

To generate a podcast interview, follow these steps:

1. Set up your AWS credentials and OpenAI API key in the `keys.py` file.
2. Run the main script:
`python podcastgenerator.py`
3. The generated interview will be saved as an MP3 file in the project directory.
