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
  "model": "gpt-4-turbo", 
  "messages": [
    {
      "role": "user",
      "content": "For 400 Portofino Drive San Carlos, CA 94070, what is the closest location we can evacuate to in case of an emergency (e.g., gas leak or fire)? Please return the results as the top 3 intersections or addresses in order of walkability."
    }
  ]
}

# Send the request
response = requests.post(url, headers=headers, json=data)

# Check for errors and parse the response
if response.status_code == 200:
    try:
        response_json = response.json()
        # Check if 'choices' exists and is non-empty
        if "choices" in response_json and response_json["choices"]:
            # Extract the content from the message
            content = response_json["choices"][0]["message"]["content"]
            print("Response Content:")
            print(content)

            # Attempt to parse the content as JSON if it's formatted as such
            try:
                parsed_response = json.loads(content)
                print("\nParsed Response as JSON:")
                print(json.dumps(parsed_response, indent=4))
            except json.JSONDecodeError:
                print("\nNote: The response is not in JSON format.")
        else:
            print("Error: 'choices' field is missing or empty in the response.")

    except (KeyError, ValueError) as e:
        print(f"Error while processing the response: {e}")
else:
    print(f"Error {response.status_code}: {response.text}")
