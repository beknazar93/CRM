from django.db import router
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
from .views import ClientViewSet

router = DefaultRouter()
router.register(r'employees', views.EmployeeViewSet )
# router.register(r'clients', views.ClientViewSet )
router.register(r'clients', ClientViewSet)
router.register(r'stages', views.SalesPipelineStageViewSet )


urlpatterns = [
    path('', include(router.urls)),

]