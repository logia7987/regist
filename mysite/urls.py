from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', views.home, name='home'),
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', views.UserRegister.as_view(), name='register'),
    url(r'^accounts/register/done/$', views.UserRegisterDone.as_view(), name='register_done'),
]
