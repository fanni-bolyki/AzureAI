import config as config
import requests
from azure.identity import DefaultAzureCredential


deployment_id = config.deployment_id
endpoint = config.endpoint
api_version = config.deployment_api_version
credential = DefaultAzureCredential()
access_token = credential.get_token("https://cognitiveservices.azure.com/.default").token

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

payload = {
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a summary of the history of space exploration."}
    ],
    "max_tokens": 100,
    "temperature": 0.7
}

# Make the request to Azure OpenAI's REST API
url = f"{endpoint}/openai/deployments/{deployment_id}/chat/completions?api-version={api_version}"
response = requests.post(url, headers=headers, json=payload)

# Check for errors
if response.status_code == 200:
    result = response.json()
    print("Response:")
    print(result["choices"][0]["message"]["content"])
else:
    print(f"Error: {response.status_code}, {response.text}")