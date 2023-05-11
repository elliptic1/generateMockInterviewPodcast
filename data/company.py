import random

tech_companies = [
    "Apple",
    "Google",
    "Microsoft",
    "Amazon",
    "Facebook",
    "Tesla",
    "IBM",
    "Intel",
    "Netflix",
    "Twitter",
    "Uber",
    "Airbnb",
    "Adobe",
    "Oracle",
    "Salesforce",
    "eBay",
    "Spotify",
    "Snap",
    "Slack",
    "Zoom",
    "Lyft",
    "Pinterest",
    "Shopify",
    "Dropbox",
    "Atlassian",
    "Square",
    "Zillow",
    "Twilio",
    "Palantir",
    "DoorDash",
    "Stripe",
    "Robinhood",
    "Coinbase",
    "Etsy",
    "Roku",
    "Splunk",
    "Docusign",
    "Akamai",
    "Snowflake",
    "Crowdstrike",
    "Datadog",
    "ServiceNow",
    "VMware",
    "Nvidia",
    "AMD",
    "Dell",
    "Cisco",
    "Zoom Video Communications",
    "Qualcomm",
    "Intuit",
    "HP",
    "OpenAI",
]


# Select a random tech company
def get_company():
    return random.choice(tech_companies)