from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import re
# Dic check login def
from django.contrib.auth import authenticate, login, decorators
from .forms import RegistrationFrom
from .forms import User
# Dic check login class base view
from django.contrib.auth.mixins import LoginRequiredMixin
class IndexClass(View):
    def get(self, request):
        return render(request, 'User/login.html')
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('pass')
        info = username+ '-' + password
        # Kiem tra user co ton tai khong
        my_User = authenticate(username = username, password = password)
        if my_User is None:
            return HttpResponse('Tài khoản không tồn tại')
        # Neu ton tai thi dang nhap
        login(request, my_User)
        messages.success(request, 'Profile details updated.')
        return redirect('http://127.0.0.1:8000/')

def register(request):
    form = RegistrationFrom()
    if request.method == 'POST':
        form = RegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Dang ki thanh cong")
    return render(request, 'User/register.html', {'form': form})

