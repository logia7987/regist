from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy

def home(requset):
    # html = '<html><div><h1>안녕하세요.</h1></div></html>'
    return render(requset, "home.html",{})
class Home(TemplateView):
    template_name = 'home.html'

class UserRegister(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserRegisterDone(TemplateView):
    template_name = 'registration/register_done.html'