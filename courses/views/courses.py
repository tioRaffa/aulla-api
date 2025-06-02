from rest_framework import generics

from courses.models import CourseModels
from courses.serializers import CourseSerializer


class CoursesApiView(generics.ListCreateAPIView):
    queryset = CourseModels
    serializer_class = CourseSerializer


class CourseApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseModels.objects.all()
    serializer_class = CourseSerializer