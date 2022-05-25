client = vonage.Client(key="ed320a43", secret="OlUMCY1dswQYQ9FD")
sms = vonage.Sms(client)


responseData = sms.send_message(
    {
        "from": "Vonage APIs",
        "to": "447594594211",
        "text": "A text message sent using the Nexmo SMS API",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")