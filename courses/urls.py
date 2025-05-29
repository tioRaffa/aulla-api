from django.urls import path
from courses.views import CoursesApiView, ReviewsApiView

urlpatterns = [
    # CURSOS
    path('courses/', CoursesApiView.as_view(), name='courses'),
    
    # AVALIAÇÕES
    path('reviews/', ReviewsApiView.as_view(), name='reviews'),
]


