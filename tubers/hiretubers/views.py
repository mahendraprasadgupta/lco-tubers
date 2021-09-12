from django.shortcuts import redirect, render
from django.contrib.messages import constants as messages
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

        #senitise all fields 
        
        hiretuber = Hiretuber(first_name = first_name,last_name = last_name,email = email,city = city, phone = phone,
                              state = state,message = message,user_id = user_id,tuber_id = tuber_id,tuber_name = tuber_name)
        hiretuber.save()
        messages.success(request, 'Thanks for reaching out !.')
        return redirect('youtubers')




    