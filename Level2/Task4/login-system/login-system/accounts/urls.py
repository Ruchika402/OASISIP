
from django.urls import path
from .views import logout_view, signup_view

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
]
