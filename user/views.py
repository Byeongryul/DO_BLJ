from django.shortcuts import render, redirect
from django.contrib import auth
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from user.models import User

from django.contrib.auth import get_user_model

from user.forms import UserRegistrationForm

class UserRegistrationView(CreateView): # 회원가입
    template_name = 'create.html'
    model = get_user_model()
    form_class = UserRegistrationForm
    success_url = '/user/login/'

class UserLoginView(LoginView):           # 로그인
    template_name = 'login.html'

    def form_invalid(self, form):
        messages.error(self.request, '로그인에 실패하였습니다.', extra_tags='danger')
        return super().form_invalid(form) 

# Create your views here.
def login(request):
    if request.method == 'POST' and User.is_active:
        return redirect('/home/')
    else:
        return render(request, 'login.html')