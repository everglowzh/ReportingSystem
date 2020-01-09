from django.urls import path
from .views import test_view_1, test_view_2, test_view_3

app_name = 'profiles'

urlpatterns = [
    path('', test_view_1, name='test_view_1'),
    path('sleep/', test_view_2, name='test_view_2'),
    path('view/', test_view_3, name='test_view_3'),
]
