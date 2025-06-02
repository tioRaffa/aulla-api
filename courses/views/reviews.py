from rest_framework import generics

from courses.models import ReviewModels
from courses.serializers import ReviewSerializer
from rest_framework.generics import get_object_or_404



class ReviewsApiView(generics.ListCreateAPIView):
    queryset = ReviewModels.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):

        if self.kwargs.get('course_pk'):
            return self.queryset.filter(course_id=self.kwargs.get('course_pk'))
        
        return self.queryset.all()


class ReviewApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReviewModels.objects.all()
    serializer_class = ReviewSerializer

    def get_object(self):
        
        if self.kwargs.get('review_pk'):
            return get_object_or_404(
                self.queryset,
                course_id=self.kwargs.get('course_pk'),
                pk=self.kwargs.get('review_pk')
            )
        
        return get_object_or_404(
            self.queryset,
            pk=self.kwargs.get('review_pk')
        )
        