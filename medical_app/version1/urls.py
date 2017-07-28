from django.conf.urls import url

from .views import create_user
from .views import login_user


urlpatterns = [
    url(r'^signup/', create_user),
    url(r'^login/', login_user),
]