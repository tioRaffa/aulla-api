from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from courses.models import ReviewModels
from courses.serializers import ReviewSerializer

class ReviewsApiViewSets(viewsets.ModelViewSet):
    queryset = ReviewModels.objects.all()
    serializer_class = ReviewSerializer