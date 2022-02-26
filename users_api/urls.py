from django.urls import path, include
from users_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('operations', views.UserViewSet, basename='operations')
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('api-view/', views.UserApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
