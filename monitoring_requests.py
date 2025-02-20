# Import the requests library to make HTTP requests
import requests

# Discord webhook URL (replace with your actual webhook URL)
WEBHOOK_URL = 'https://discord.com/api/webhooks/1339212805026349089/2ECYQF4SAb7SLnF-UgRGqrgwrPLGGl0gtIESdFK45nxuEcHj2zJZvhxRHMTs56idTxTJ'

# List of websites to check, each with a URL and a string to search for in the content
websites_list = [
    {
        "url": "https://wwebdesign.co.uk",
        "string_to_match": "W Web Design"
    }, {
        "url": "https://google.com/nothere",
        "string_to_match": "Google"
    },{
        "url": "https://www.terahost.co.uk",
        "string_to_match": "Support"
    }
]

# Function to send a notification to Discord using the webhook
def send_discord_notification(message):
    """Send a message to Discord using a webhook."""
    # Create the payload (message content) to send to Discord
    payload = {
        "content": message
    }
    # Send the payload to the Discord webhook URL as a POST request
    response = requests.post(WEBHOOK_URL, json=payload)
    # Check if the request was successful (status code 204 means success)
    if response.status_code == 204:
        print("Discord notification sent successfully!")
    else:
        # If the request failed, print the error status code
        print(f"Failed to send Discord notification. Status code: {response.status_code}")

# Loop through each website in the list
for website in websites_list:
    # Print a blank line for readability
    print()
    # Print the URL of the website being checked
    print(f"Checking website: {website['url']}")

    # Send an HTTP GET request to the website and store the response
    response = requests.get(website['url'])

    # Check if the HTTP status code is not 200 (indicating an error)
    if response.status_code != 200:
        # Create an error message with the URL and status code
        error_message = f"Error on site {website['url']}! Status code received: {response.status_code}"
        # Print the error message
        print(error_message)
        # Send the error message to Discord
        send_discord_notification(error_message)
    else:
        # If the status code is 200, create a success message
        success_message = f"Status code is OK for {website['url']}! Status code received: {response.status_code}"
        # Print the success message
        print(success_message)

        # Check if the string_to_match is NOT in the website's content
        if website['string_to_match'] not in response.text:
            # Create a message indicating the string was not found
            not_found_message = f"{website['string_to_match']} not found on {website['url']}!"
            # Print the not found message
            print(not_found_message)
            # Send the not found message to Discord
            send_discord_notification(not_found_message)
        else:
            # If the string_to_match is found, create a success message
            found_message = f"{website['string_to_match']} found on {website['url']}!"
            # Print the found message
            print(found_message)
            # Send the found message to Discord
            send_discord_notification(found_message)

            # Print a blank line for readability
        