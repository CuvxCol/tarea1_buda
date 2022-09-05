from rest_framework.routers import DefaultRouter
from posixpath import basename
from api.views import spread, trial
from django.urls import path

router = DefaultRouter()

router.register(r'trial', trial.CrudViewSet, basename='trial')

route_spread = [
     path('spread/<str:market_id>/', spread.RetrieveAPIView.as_view(), name='spread.retrieve'),
     path('spread/<str:market_id>/save/', spread.SaveAPIView.as_view(), name='spread.create'),
     path('spread/<str:market_id>/last_save/', spread.LastSavedAPIView.as_view(), name='spread.last_save'),
     path('spread/', spread.ListAPIView.as_view(), name='spread.list'),
]

urlpatterns = \
     router.urls + \
     route_spread