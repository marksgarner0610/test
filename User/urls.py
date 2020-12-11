from django.urls import path, include
from .views import IndexClass
from . import views
app_name = 'login'
urlpatterns = [
    path('', IndexClass.as_view() ,name = 'login' ),
    path('register/', views.register, name = 'register'),
]