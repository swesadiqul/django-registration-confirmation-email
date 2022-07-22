from django.urls import path  
from .views import home, signup, activate  
urlpatterns = [  
    path('', home, name = 'home'),  
    path('form/', signup, name = 'signup'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),  
]