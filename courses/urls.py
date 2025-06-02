from django.urls import path
from courses.views import CoursesApiView, CourseApiView, ReviewsApiView, ReviewApiView

urlpatterns = [
    # CURSOS
    path('courses/', CoursesApiView.as_view(), name='courses'),
    path('courses/<int:pk>/', CourseApiView.as_view(), name='course'),

    path('courses/<int:course_pk>/reviews/', ReviewsApiView.as_view(), name='course reviews'),
    path('courses/<int:course_pk>/reviews/<int:review_pk>/', ReviewApiView.as_view(), name='course review'),
    
    # AVALIAÇÕES
    path('reviews/', ReviewsApiView.as_view(), name='reviews'),
    path('reviews/<int:review_pk>/', ReviewApiView.as_view(), name='review'),
]


