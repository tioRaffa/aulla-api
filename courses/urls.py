from django.urls import path
from courses.views import CourseApiView, ReviewApiView

urlpatterns = [
    # CURSOS
    path('courses/', CourseApiView.as_view(), name='courses'),
    
    # AVALIAÇÕES
    path('reviews/', ReviewApiView.as_view(), name='reviews'),
]


