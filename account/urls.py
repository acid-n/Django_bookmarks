from django.urls import path
from . import views

urlpatterns = [
    # Обработчик действий со статьями
    path('login/', views.user_login, name='login'),
]