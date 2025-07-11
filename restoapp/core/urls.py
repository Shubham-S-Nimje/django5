from django.urls import path
from core.views import home, menu, ordertrack, contact, reservation

urlpatterns = [
    path('', home, name='restoapp home'),
    path('menu', menu, name='menu'),
    path('order-track', ordertrack, name='ordertrack'),
    path('reservation', reservation, name='reservation'),
    path('contact', contact, name='contact')
]
