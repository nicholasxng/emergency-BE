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
  "role": "system",
  "content": "As an AI language model, you should respond **only** with a JSON object containing non-emergency phone numbers for the given address. Use exactly these keys: 'fire', 'police', 'medical', 'poison', 'gas_leak', and 'animal_control'. If a number is not available, set the value to 'No information available'. Do not include any additional text outside the JSON object."
},
    {
      "role": "user",
      "content": "Provide non-emergency phone numbers for fire, police, medical, poison, and gas leak for 400 Portofino Drive San Carlos, CA 94070"
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
