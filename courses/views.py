from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
    
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class ReviewApiView(APIView):

    def get(self, request):
         reviews = ReviewModels.objects.all()
         serializer = ReviewSerializer(reviews, many=True)

         return Response(serializer.data)
    
    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)