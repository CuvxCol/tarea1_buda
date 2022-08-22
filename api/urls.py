from rest_framework.routers import DefaultRouter
from posixpath import basename
from api import views
from django.urls import path, include

router = DefaultRouter()

router.register(r'test', views.TestView, basename='test')

urlpatterns = router.urls

# urlpatterns = [
#     path('test/', views.TestView.as_view(), basename='test'),
# ]