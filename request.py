import requests
import json

url = "https://graph.facebook.com/v16.0/116532644672367/messages"
headers = {
    "Authorization": "Bearer EAAg6yhcRlLkBANopH8ZBH8ZAhXiJNwqKKFgsP6aA9DXw9RVW5KdZChE16QOZCDylSoCofEddCwHLbzaBTSyjZCEuQNgfZCmWlOEFVyUcEHkDtCNxljEJ62KriQZAbTqXWbFgHlOPF2EHGdOA8z7neCjzha3djE99Gq9PLveVp3uYBRJOmi0626lbZAVGH6xKcFMSK70Ss35UfUceGo5FPZArX",
    "Content-Type": "application/json"
}
data = {
    "messaging_product": "whatsapp",
    "to": "573013369276",
    "text": {
        "body": "helworld"
        }
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    print("Message sent successfully!")
else:
    print(f"Error: {response.status_code} - {response.text}")
