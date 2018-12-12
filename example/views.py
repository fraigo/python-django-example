from django.shortcuts import render
from django.http import HttpResponse
from example.models import Sender, Message

def index(request):
    try:
        messages = Message.objects.all()
    except:
        messages = []
    content = []
    for message in messages:
        content.append('<div style="border:1px solid gray;padding:5px">')
        content.append('<div><b>From:</b> %s </div>' % message.sender )
        content.append('<div><b>To:</b> %s </div>' % message.recipient )
        content.append('<div><b>Date:</b> %s </div>' % message.timestamp )
        content.append('<pre>%s</pre>' % message.message )
        content.append('</div>')
    return HttpResponse('<h1>Messages</h1> %s' % ('\n'.join(content) ) )
