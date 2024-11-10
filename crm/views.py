from rest_framework import viewsets
from .models import Employee,Client,SalesPipelineStage
from .serializers import EmployeeSerializer,ClientSerializer,SalesPipelineStageSerializer



class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class SalesPipelineStageViewSet(viewsets.ModelViewSet):
    queryset = SalesPipelineStage.objects.all()
    serializer_class = SalesPipelineStageSerializer
