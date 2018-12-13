import datetime
from example.models import Message, Sender

sender = Sender(name="Me Myself", email="me@myself.com", imageUrl="")
sender.save()
recipient = Sender(name="You Yourseld", email="you@yourself.com", imageUrl="")
recipient.save()
message = Message(
    sender=sender,
    recipient=recipient,
    message="Hello! How are you?",
    timestamp=datetime.datetime.now()
    )
message.save()
