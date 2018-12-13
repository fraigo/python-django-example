import datetime
from example.models import Message, Sender

sender = Sender(name="Me Myself", email="me@myself.com", imageUrl="")
recipient = Sender(name="You Yourseld", email="you@yourself.com", imageUrl="")
message = Message(
    sender=sender,
    recipient=recipient,
    message="Hello! How are you?",
    timestamp=datetime.datetime.now()
    )
