# chat/views.py

from django.shortcuts import render
from .models import Message
from users.models import CustomUser


def chat(request, user_id):
    # Display chat between the logged-in user and another user (seller or buyer)
    user = CustomUser.objects.get(id=user_id)
    messages = Message.objects.filter(sender=request.user, receiver=user) | Message.objects.filter(sender=user,
                                                                                                   receiver=request.user)
    messages = messages.order_by('timestamp')  # Order messages by timestamp

    if request.method == 'POST':
        content = request.POST.get('message')
        Message.objects.create(sender=request.user, receiver=user, content=content)
        return redirect('chat', user_id=user.id)

    return render(request, 'chat.html', {'user': user, 'messages': messages})