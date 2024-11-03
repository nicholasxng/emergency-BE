import requests

api_key = "sk-svcacct-OFKDT4n936sRFkYLqmXH1NSJajS-ow3fJ2ww98RM2L-R5whsyxxgTz10GnDSCzZKlqYFT3BlbkFJIiFrIjHlBvC_ZM4QBqEVIup1OV1QwIxkmLlq7nJzvxP1drMA1t6AykqSlMXSdZzhmu4A"
endpoint = "https://api.openai.com/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "model": "gpt-3.5-turbo",  # Use "gpt-4" if you have access to it
    "messages": [{"role": "user", "content": "give me the weather for 94070"}],
    "temperature": 0.7
}

response = requests.post(endpoint, headers=headers, json=data)

if response.status_code == 200:
    print(response.json()["choices"][0]["message"]["content"])
else:
    print("Error:", response.status_code, response.text)
