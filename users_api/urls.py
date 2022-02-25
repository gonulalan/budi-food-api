from django.urls import path
from users_api import views


urlpatterns = [
    path('operations/', views.UserApiView.as_view()),
]
