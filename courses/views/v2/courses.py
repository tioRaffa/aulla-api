from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from courses.models import CourseModels, ReviewModels
from courses.serializers import CourseSerializer, ReviewSerializer


class CoursesApiViewSets(viewsets.ModelViewSet):
    queryset = CourseModels.objects.all()
    serializer_class = CourseSerializer


    @action(detail=True, methods=['get'])
    def reviews(self, request, pk=None):

        self.pagination_class.page_size = 1
        reviews = ReviewModels.objects.filter(course_id=pk)
        page = self.paginate_queryset(reviews)

        if page is not None:
            serializer = ReviewSerializer(page, many=True)
            return Response(serializer.data)

        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)