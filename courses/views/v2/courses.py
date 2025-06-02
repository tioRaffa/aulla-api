from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from courses.models import CourseModels
from courses.serializers import CourseSerializer, ReviewSerializer


class CoursesApiViewSets(viewsets.ModelViewSet):
    queryset = CourseModels.objects.all()
    serializer_class = CourseSerializer


    @action(detail=True, methods=['get'])
    def reviews(self, request, pk=None):

        course = self.get_object()
        serializer = ReviewSerializer(course.reviews.all(), many=True)
        
        return Response(serializer.data)