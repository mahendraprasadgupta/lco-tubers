from django.shortcuts import redirect, render
from django.contrib import messages
from . models import Hiretuber

# Create your views here.


def hiretuber(request):

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        city = request.POST['city']
        phone = request.POST['phone']
        state = request.POST['state']
        message = request.POST['message']

        user_id = request.POST['user_id']

        tuber_id = request.POST['tuber_id']
        tuber_name = request.POST['tuber_name']

        # senitise all fields
        if not first_name or not last_name or not email or not phone or not state or not city or not message:
            messages.warning(request, 'All fields are required to be filled.')
            return redirect('youtubers_detail', id=tuber_id)

        hiretuber = Hiretuber(first_name=first_name, last_name=last_name, email=email, city=city, phone=phone,
                              state=state, message=message, user_id=user_id, tuber_id=tuber_id, tuber_name=tuber_name)
        hiretuber.save()
        messages.success(request, 'Thanks for reaching out !.')
        return redirect('youtubers')
