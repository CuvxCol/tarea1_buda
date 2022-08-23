from rest_framework.routers import DefaultRouter
from posixpath import basename
from api import views
from django.urls import path, include

router = DefaultRouter()

router.register(r'test', views.TestView, basename='test')
# router.register(r'spread', views.SpreadView, basename='spread')

urlpatterns = router.urls + [
     path('spread/<str:market_id>/', views.SpreadView.as_view(), name='spread'),
]

# urlpatterns = [
#     path('test/', views.TestView.as_view(), basename='test'),
# ]