from django.urls import path
from courses.views import CoursesApiView, CourseApiView, ReviewsApiView, ReviewApiView

urlpatterns = [
    # CURSOS
    path('courses/', CoursesApiView.as_view(), name='courses'),
    path('course/<int:pk>/', CourseApiView.as_view(), name='course'),
    
    # AVALIAÇÕES
    path('reviews/', ReviewsApiView.as_view(), name='reviews'),
    path('review/<int:pk>/', ReviewApiView.as_view(), name='review'),
]


