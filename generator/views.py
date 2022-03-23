from django.shortcuts import render
from django.http import HttpResponse
import random
import string

# Create your views here.


def home(request):
    return render(request, 'generator/home.html',)


def password(request):
    # print(string.printable)
    length = int(request.GET.get('length', 12))
    listpassword = []
    listpassword.extend(list(string.ascii_lowercase))

    if request.GET.get('uppercase'):
        ucase = string.ascii_uppercase
        listpassword.extend(list(ucase))

    if request.GET.get('numbers'):
        num = string.digits
        listpassword.extend(list(num))

    if request.GET.get('special'):
        punc = string.punctuation
        listpassword.extend(list(punc))

    thepassword = ""

    for len in range(length):

        thepassword += random.choice(listpassword)

    return render(request, 'generator/password.html', {'password': thepassword})
