from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student
from rest_framework.pagination import PageNumberPagination


class StudentPagination(PageNumberPagination):
    page_size = 1


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = PageNumberPagination
