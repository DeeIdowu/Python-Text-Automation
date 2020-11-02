"""Step 1: [Text Messages] have a collection/array of preset messages sent via my_messages = [" ", ""]"""


from twilio.rest import Client
GOOD_MORNING_QUOTES = [
    "Good Morning Love!",
    "How are you doing today?"
]

"""Step: 2: [Send to S/O] Send Preset Message Using API send_message(my_messages[0])"""

"""Creation of function for the twilio API"""
cellphone = 123,
twilio_number = 234


def send_message(quote):
    account = "AC011b8f39d3022b8b0ce98de3afb723f3"
    token = "41558565abcd668d361b4eb494ee679f"
    client = Client(account, token)

    client.messages.create(to=cellphone,
                           from=twilio_number,
                           body=quote)
