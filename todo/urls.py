from django.conf.urls import url
from django.contrib.auth.views import login, logout

from . import views

app_name = 'todo'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'login_view', views.login_view, name='login_view'),
    url(r'logout_view', views.logout_view, name='logout_view'),
]