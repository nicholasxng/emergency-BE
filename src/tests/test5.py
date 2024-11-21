import openai
import os

def get_emergency_contact_info(address):
    openai.api_key = "sk-svcacct-OFKDT4n936sRFkYLqmXH1NSJajS-ow3fJ2ww98RM2L-R5whsyxxgTz10GnDSCzZKlqYFT3BlbkFJIiFrIjHlBvC_ZM4QBqEVIup1OV1QwIxkmLlq7nJzvxP1drMA1t6AykqSlMXSdZzhmu4A"
    
    prompt = f"""
    Provide verified emergency contact information for 400 portofino drive #3 San Carlos CA 94070 in a table format. The table should include the following emergency contacts: General emergency number, local police department, county sheriff, fire department, nearest hospital, Poison Control (with both a physical location and phone number), nearby veterinarian, local animal shelter, power company, water company (confirmed to serve the address), and the local Red Cross.
    
    Each row should contain:
    Name (of the service)
    Address (or nearest intersection if no exact address is available)
    Distance from Address (in miles)
    Phone Number
    Email (if available)
    City
    County
    State
    
    Verify each contact with at least two reputable sources, such as the service provider’s official website or the city/county website. Clearly state any uncertainties if conflicting information exists or if confirmation cannot be obtained directly. Ensure each utility provider serves the specified address before including it.
    """

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1500,
        temperature=0.5
    )

    return response.choices[0].text.strip()

if __name__ == "__main__":
    address = "400 Portofino Drive, San Carlos, CA"
    emergency_contact_info = get_emergency_contact_info(address)
    print(emergency_contact_info)
