from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^signup/', views.SignUp.as_view(), name='signup'),
]
