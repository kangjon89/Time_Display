from django.shortcuts import render
from datetime import datetime

def index(request):
    context = {
        "time": datetime.now().strftime("%I:%M %p"),
        'date': datetime.now().strftime("%m-%d-%Y")
    }
    return render(request,'index.html', context)
