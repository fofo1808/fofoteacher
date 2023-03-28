import os
import json
import requests

api_key = "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" # Make sure your API key is stored as an environment variable

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

data = {
    "model": "gpt-4",
    "messages": [
        {"role": "system", "content": "You are an english teacher"},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, data=json.dumps(data))

if response.status_code == 200:
    response_data = response.json()
    print("Full response (pretty printed):")
    print(json.dumps(response_data, indent=2))

    generated_text = response_data["choices"][0]["message"]["content"]
    print("Generated text:", generated_text)
else:
    print(f"Error: {response.status_code} - {response.text}")
