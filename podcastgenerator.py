import boto3
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import OutputParserException

from data.company import get_company
from data.job_titles import get_job_title
from keys import OpenAI_API_KEY, aws_access_key_id, aws_secret_access_key
from data.senior_job_titles import get_senior_job_title
from speech_util import create_audio_files
from util import remove_files, concatenate_audio_files
from data.voices import get_interviewee_voice

remove_files()

max_content_tokens = 1000  # Reserve some tokens for the other messages and instructions.

chat = ChatOpenAI(openai_api_key=OpenAI_API_KEY)

# This is to get a random tech job title
company = get_company()
interviewer_title = get_senior_job_title()
job_post_title = get_job_title()
interviewee_voice = get_interviewee_voice()
user_input = ""
num_questions = 10
interviewer_voice = "Arthur"

# Commented out IPython magic to ensure Python compatibility.
response_schemas = [
    ResponseSchema(name="Introduction", description="This is an introduction to the interview"),
    ResponseSchema(name="Outro", description="This is an outro for the interview"),
]

# How you would like to parse your output
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

system_template = """
This is a podcast where we give mock technical interviews to people who are guests on the podcast.
You are the podcast host and are also pretending to be a {interviewer_title} from {company}, and you interviewing a person for the job of {job_post_title}.
Research the company {company}, its business practices, ideology, and its technologies.
Generate the intro and outro for the interview. The intro should contain information about {company} and thank the guest, whose name is {interviewee_voice}.
The outro should thank the guest, {interviewee_voice}, and thank the audience and ask people to subscribe to the podcast.
"""

system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

human_template = """

{format_instructions}

# % USER INPUT:
{user_input}

YOUR RESPONSE:
"""

human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

_input = chat_prompt.format_prompt(
    format_instructions=output_parser.get_format_instructions(),
    user_input=user_input,
    interviewer_title=interviewer_title,
    interviewee_voice=interviewee_voice,
    company=company,
    job_post_title=job_post_title,
)

output = chat(_input.to_messages())

try:
    intro_outro_response_json = output_parser.parse(output.content)
except OutputParserException:
    intro_outro_response_json = {}

# Commented out IPython magic to ensure Python compatibility.
response_schemas = [
    ResponseSchema(name="Question1", description="This is question 1"),
    ResponseSchema(name="Answer1", description="This is answer 1"),
    ResponseSchema(name="Question2", description="This is question 2"),
    ResponseSchema(name="Answer2", description="This is answer 2"),
]

# How you would like to parse your output
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

system_template = f"""
This is a podcast where we give mock technical interviews to people who are guests on the podcast.
You are the podcast host and are also pretending to be a {interviewer_title} from {company}, and you interviewing a person for the job of {job_post_title}.
Research the company {company}, its business practices, ideology, and its technologies.
Ask technical and system and behavioral interview questions related to the job of {job_post_title}, from the point of view of a {interviewer_title} from {company}.
Generate {num_questions} questions and answers in valid JSON.
There should be no markdown, no formatting, no newlines, no quotation marks, and no tabs in your response.
All output should be valid parsable json.
"""

system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

human_template = """

{format_instructions}

# % USER INPUT:
{user_input}

YOUR JSON CODE RESPONSE:
"""

human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

_input = chat_prompt.format_prompt(
    format_instructions=output_parser.get_format_instructions(),
    user_input=user_input,
    interviewer_title=interviewer_title,
    company=company,
    job_post_title=job_post_title,
    num_questions=num_questions,
)

output = chat(_input.to_messages())

try:
    response_json = output_parser.parse(output.content)
except OutputParserException:
    response_json = {}

# Create a client using the credentials and region defined in your AWS configuration
polly_client = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name='us-east-1'
).client('polly')

# Create the audio files
filenames = create_audio_files(response_json, interviewee_voice, num_questions,
                               intro_outro_response_json, interviewer_voice, polly_client)

# Concatenate the audio files
concatenate_audio_files(filenames)
