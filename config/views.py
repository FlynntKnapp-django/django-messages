from django.contrib import messages
from django.shortcuts import render


def messages_view(request):
    """
    A view that displays a message.
    """
    messages.info(request, "This is the first custom message!", extra_tags="info")
    messages.info(request, "This is the second custom message!", extra_tags="success")
    messages.info(request, "This is the third custom message!", extra_tags="warning")
    return render(request, "index.html")
