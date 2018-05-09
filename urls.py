from django.urls import path
from . import views
urlpatterns = [
    path('',views.login,name='login'),
    path('index/',views.post,name='post'),
    path('complete/',views.index,name='index'),
]
