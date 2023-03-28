import os
import json
import requests
from dotenv import load_dotenv

def send_whatsapp_message(to_phone_number, message_text):
    load_dotenv()

    url = "https://graph.facebook.com/v16.0/116532644672367/messages"
    auth_token = os.getenv("AUTH_TOKEN")
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    data = {
        "messaging_product": "whatsapp",
        "to": to_phone_number,
        "text": {
                "body": message_text
            
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    recipient_phone_number = "573013369276"
    message = "Hello, this is a test message from the WhatsApp Business API!"
    send_whatsapp_message(recipient_phone_number, message)
