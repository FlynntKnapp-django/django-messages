from django.contrib import messages
from django.shortcuts import render


def messages_view(request):
    """
    A view that displays a message.
    """
    messages.info(request, "This is the first custom message!")
    messages.info(request, "This is the second custom message!")
    return render(request, "index.html")
