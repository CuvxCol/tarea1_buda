from rest_framework.routers import DefaultRouter
from posixpath import basename
from api.views import spread, trial
from django.urls import path

router = DefaultRouter()

router.register(r'trial', trial.CrudViewSet, basename='trial')

route_spread = [
     path('spread/<str:market_id>/', spread.RetrieveAPIView.as_view(), name='spread.retrieve'),
]

urlpatterns = \
     router.urls + \
     route_spread