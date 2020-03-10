# GUI for senior design
# logic for GUI
# Input IF numbers> once the proper character
# numbers then light up the start button>
# have emergency stop light up>
# Once complete will auto stop and return to
# the main screen.

INSTALLED_APPS - [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Bridgebreaker',
    'crispy_forms',
    ]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

from django.shortcuts import render

def Bridgebreaker(request):
    return render(request, 'Bridgebreaker.html',{})

