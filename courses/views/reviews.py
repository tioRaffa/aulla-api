from rest_framework import generics

from courses.models import ReviewModels
from courses.serializers import ReviewSerializer


class ReviewsApiView(generics.ListCreateAPIView):
    queryset = ReviewModels.objects.all()
    serializer_class = ReviewSerializer


class ReviewApiView(generics.RetrieveUpdateDestroyAPIView):
    pass