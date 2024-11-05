import requests
import json

# Set up your OpenAI API key
api_key = "sk-svcacct-OFKDT4n936sRFkYLqmXH1NSJajS-ow3fJ2ww98RM2L-R5whsyxxgTz10GnDSCzZKlqYFT3BlbkFJIiFrIjHlBvC_ZM4QBqEVIup1OV1QwIxkmLlq7nJzvxP1drMA1t6AykqSlMXSdZzhmu4A"

# Define the endpoint and headers
url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Define the JSON body of the request
data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "user",
            "content": (
                "For this address: 123 Main St, please return the non-emergency phone numbers as a JSON array. "
                "Each entry should have 'service' (e.g., 'Police') and 'number' (e.g., '650-802-4277') fields. "
                "Include non-emergency numbers for fire, police, medical, poison, gas leak, and animal control. "
                "If any service information is not available, set 'number' to 'No information available'. "
                "Do not format the response as a code block."
            )
        }
    ]
}

# Send the request
response = requests.post(url, headers=headers, json=data)

# Check for errors and parse the response
if response.status_code == 200:
    response_json = response.json()
    try:
        # Extract the content from the message
        content = response_json["choices"][0]["message"]["content"]
        # Print the structured response
        print("Response Content:")
        print(content)

        # Optionally, convert the response content to a Python list if it’s valid JSON
        try:
            parsed_response = json.loads(content)
            print("\nParsed Response as JSON:")
            print(json.dumps(parsed_response, indent=4))
        except json.JSONDecodeError:
            print("\nError: Response is not valid JSON.")

    except KeyError as e:
        print(f"KeyError: {e}")
else:
    print(f"Error {response.status_code}: {response.text}")
