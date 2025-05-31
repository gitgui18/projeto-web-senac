from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('how-to-play/', views.how_to_play, name='how_to_play'),
    path('settings/', views.settings_view, name='settings'),  # ✅ aqui também
    path('about/', views.about, name='about'),
    path('play/', views.play, name='play'),  
]
