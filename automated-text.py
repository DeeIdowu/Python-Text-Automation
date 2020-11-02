"""Step 1: [Text Messages] have a collection/array of preset messages sent via my_messages = [" ", ""]"""
from twilio.rest import Client
import schedule
import random

GOOD_MORNING_QUOTES = [
    "Good Morning Love!",
    "How are you doing today?"
]

"""Step: 2: [Send to S/O] Send Preset Message Using API send_message(my_messages[0])"""

"""Creation of function for the twilio API""":


cellphone = 123,
twilio_number = 234


def send_message(quote):
    account = "AC011b8f39d3022b8b0ce98de3afb723f3"
    token = "41558565abcd668d361b4eb494ee679f"
    client = Client(account, token)
    client.messages.create(to=cellphone,
                           from=twilio_number,
                           body=quote)


"""Step 3: [Every Morning] Use Library to Schedule a text to S/O 
@ Specific Time via use of Schedule Library API & Randomly selecting quotes via random library"""
quote = GOOD_MORNING_QUOTES[random.randint(0, len(GOOD_MORNING_QUOTES))]
schedule.every().day.at("6:30").do(send_message, quote)
