from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CourseModels, ReviewModels
from .serializers import CourseSerializer, ReviewSerializer
# Create your views here.


class CourseApiView(APIView):
    """
    API RESTFULL
    """
    def get(self, request):
        courses = CourseModels.objects.all()
        serializer = CourseSerializer(courses, many=True)
        
        return Response(serializer.data)
    

class ReviewApiView(APIView):

    def get(self, request):
         reviews = ReviewModels.objects.all()
         serializer = ReviewSerializer(reviews, many=True)

         return Response(serializer.data)