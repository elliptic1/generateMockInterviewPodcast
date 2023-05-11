# This is to get a random tech job title

import random

# List of 50 unique tech job titles
tech_jobs = [
    'Software Developer',
    'Data Scientist',
    'Database Administrator',
    'Systems Analyst',
    'Network Administrator',
    'Information Security Analyst',
    'AI Specialist',
    'Web Developer',
    'Cloud Solutions Architect',
    'IT Manager',
    'IT Project Manager',
    'Product Manager',
    'Mobile Application Developer',
    'Front-End Developer',
    'Back-End Developer',
    'Full Stack Developer',
    'DevOps Engineer',
    'Quality Assurance Tester',
    'UI/UX Designer',
    'Technical Support Specialist',
    'Business Intelligence Analyst',
    'SEO Specialist',
    'Data Analyst',
    'Cybersecurity Specialist',
    'Software Engineer',
    'Hardware Engineer',
    'IT Consultant',
    'Python Developer',
    'Java Developer',
    'Ruby Developer',
    'PHP Developer',
    'C# Developer',
    'C++ Developer',
    'Javascript Developer',
    'iOS Developer',
    'Android Developer',
    'Machine Learning Engineer',
    'Data Engineer',
    'Network Engineer',
    'Salesforce Developer',
    'Embedded Systems Engineer',
    'Game Developer',
    'Virtual Reality Developer',
    'IT Coordinator',
    'IT Director',
    'Chief Technology Officer',
    'Blockchain Developer',
    'Systems Engineer',
    'Big Data Engineer',
    'Cloud Consultant'
]


# Pick a random job title from the list
def get_job_title():
    return random.choice(tech_jobs)
