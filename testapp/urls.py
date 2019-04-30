from django.urls import path

from . import views as c_views

app_name = 'testapp'
urlpatterns = [
    path(r'', c_views.IndexView.as_view(), name='index'),
]