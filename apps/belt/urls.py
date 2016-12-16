from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^poker/(?P<user_id>\d*)$', views.add_poke),
]
