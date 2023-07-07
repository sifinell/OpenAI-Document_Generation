import openai
# import os

# Get the API key and resource endpoint from environment variables
API_KEY = "your-openai-key"
RESOURCE_ENDPOINT = "your-openai-endpoint"

# Set the API type and key in the openai library
openai.api_type = "azure"
openai.api_key = API_KEY
openai.api_base = RESOURCE_ENDPOINT
openai.api_version = "2022-12-01"

COMPLETIONS_MODEL = "davinci"

# Set the parameter for the completions API call
COMPLETIONS_API_PARAMS = {
    # We use temperature of 0.3 to generate more interesting and varied completions.
    "temperature": 0.3,
    "max_tokens": 2000,
    "engine": COMPLETIONS_MODEL,
}

def prompt_open_ai(prompt, paragraph):
    prompt = prompt + " " + paragraph

    response = openai.Completion.create(
                #engine=COMPLETIONS_MODEL,
                prompt=prompt,
                **COMPLETIONS_API_PARAMS
            )

    return response["choices"][0]["text"]
