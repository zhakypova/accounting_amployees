from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Position, Employees
from .serializers import PositionSerializer, EmployeesSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['department', 'name_position']
    search_fields = ['department', 'name_position']


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['fullname', 'salary']
    search_fields = ['fullname', ]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

