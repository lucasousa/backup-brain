from django.urls import path
from .views import *


app_name = 'wiki'

urlpatterns = [
    path('criar', WikiCreate.as_view(), name='new_wiki'),

]